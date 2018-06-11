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

build_docker.alpine: Dockerfile.alpine app
	sudo docker build -f Dockerfile.alpine -t kollerr/nabla-node-webrepl:alpine .

run_docker.alpine:
	sudo docker run --rm -it --expose=8081 --cap-add=NET_ADMIN \
		kollerr/nabla-node-webrepl:alpine \
		--volume app:/app /app/app.js

run_docker.rootfs:
	# XXX: hack used to have a /dev/urandom inside of the unikernel
	dd if=/dev/random of=/tmp/urandom count=1 bs=1024
	sudo docker run --rm -it --expose=8081 --cap-add=NET_ADMIN \
		-v /tmp/urandom:/home/node/dev/urandom \
		kollerr/nabla-node-webrepl:alpine \
		--volume /home/node/:/ /app/app.js
