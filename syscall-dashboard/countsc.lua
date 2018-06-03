-- Chisel description
description = "counts how many times the specified system call has been called"
short_description = "syscall count"
category = "misc"

require "common"
json = require ("dkjson")


-- Chisel argument list
args = {}

count = 0
crtable = {}

-- https://github.com/draios/sysdig/blob/8d0fcfd2bf2b735e066da7c8e658b49cb9d5c413/userspace/sysdig/chisels/spy_users.lua

function on_init()
	ftype = chisel.request_field("evt.type")
	fdir = chisel.request_field("evt.dir")
	ffdnum = chisel.request_field("fd.num")
	chisel.set_filter("evt.type != switch and evt.dir = <") -- only get these ones
	--chisel.set_filter("evt.type != switch and evt.dir = >") -- only get these ones
	return true
end

function on_capture_start()
	chisel.set_interval_ns(1000000000)
	return true
end

-- on_interval
--
-- Event parsing callback
function on_event()
	fdnum = evt.field(ffdnum)
	if fdnum ~= nil and fdnum > 0 then
		key = evt.field(ftype) .. "(" .. tostring(fdnum) .. ")"
	else
		key = evt.field(ftype)
	end

	entryval = crtable[key]
	if entryval == nil then
		crtable[key] = 1
	else
		crtable[key] = crtable[key] + 1
	end
	count = count + 1
	return true
end

TOP_NUMBER = 0


-- End of capture callback
function on_interval(ts_s, ts_ns, delta)
	local str = json.encode(crtable, { indent = false })
	print(str)
 	return true
end

-- End of capture callback
function on_capture_end()
 	return true
end
