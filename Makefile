# Copyright (c) 2018 Contributors as noted in the AUTHORS file
#
# Permission to use, copy, modify, and/or distribute this software
# for any purpose with or without fee is hereby granted, provided
# that the above copyright notice and this permission notice appear
# in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
# WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
# AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
# OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

all:
	@echo "To build a demo image, run 'make'"
	@echo "in the demo's directory."
	@echo
	@echo "To build all demo images, run 'make world'."

world:
	make -C node-express
	make -C node-webrepl
	make -C python-tornado
	make -C redis-test

publish: world
	sudo docker tag node-express-nabla nablact/node-express-nabla:v0.2
	sudo docker tag node-express-legacy nablact/node-express-legacy:v0.2
	sudo docker tag node-webrepl-nabla nablact/node-webrepl-nabla:v0.2
	sudo docker tag node-webrepl-legacy nablact/node-webrepl-legacy:v0.2
	sudo docker tag python-tornado-nabla nablact/python-tornado-nabla:v0.2
	sudo docker tag python-tornado-legacy nablact/python-tornado-legacy:v0.2
	sudo docker tag redis-test-nabla nablact/redis-test-nabla:v0.2
	sudo docker tag redis-test-legacy nablact/redis-test-legacy:v0.2
	sudo docker push nablact/node-express-nabla:v0.2
	sudo docker push nablact/node-express-legacy:v0.2
	sudo docker push nablact/node-webrepl-nabla:v0.2
	sudo docker push nablact/node-webrepl-legacy:v0.2
	sudo docker push nablact/python-tornado-nabla:v0.2
	sudo docker push nablact/python-tornado-legacy:v0.2
	sudo docker push nablact/redis-test-nabla:v0.2
	sudo docker push nablact/redis-test-legacy:v0.2
