# Copyright (c) 2018, IBM
# Author(s): Brandon Lum, Ricardo Koller
#
# Permission to use, copy, modify, and/or distribute this software for
# any purpose with or without fee is hereby granted, provided that the
# above copyright notice and this permission notice appear in all
# copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
# WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
# AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
# DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA
# OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
# TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.

build_docker.alpine: Dockerfile.alpine
	sudo docker build -f Dockerfile.alpine -t kollerr/nabla-python3-tornado:alpine .

run_docker.alpine:
	sudo docker run --rm -it --expose=5000 --cap-add=NET_ADMIN \
		kollerr/nabla-python3-tornado:alpine \
		--env PYTHONHOME=/python -- /python/tornado_main.py

run_docker.rootfs:
	# XXX: hack used to have a /dev/urandom inside of the unikernel
	dd if=/dev/random of=/tmp/urandom count=1024 bs=1024
	# We use this `--volume /usr:/`, so our hacky /dev/urandom
	# has to be at /usr/dev/urandom
	sudo docker run --rm -it --expose=5000 --cap-add=NET_ADMIN \
		-v /tmp/urandom:/usr/dev/urandom \
		-v $(CURDIR)/rootfs/etc:/usr/etc \
		kollerr/nabla-python3-tornado:alpine \
		--env PYTHONHOME=/local \
		--volume /usr:/ -- /local/tornado_main.py
