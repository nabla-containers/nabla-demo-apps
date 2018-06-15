This repository holds some containerized applications that we use for
testing and also serves the purpose of showing how to run your own
applications using the nabla container bases from the
[nabla-base-build](https://github.com/nabla-containers/nabla-base-build)
repository.

Each subdirectory contains two Dockerfiles (`Dockerfile` for a
standard container and `Dockerfile.nabla` for a nabla container) and a
Makefile that builds both standard and nabla containers of the
application (for comparison purposes).  For example, to build the
`node-express` application, just:

    cd node-express
    make

### Running the Containers

The `Makefile` will produce two container images, named after the
directory (the test application name) with and without "-nabla"
appended to the end.  To run the applications, use Docker (you must
have installed [`runnc`](https://github.com/nabla-containers/runnc)
for the nabla case).  For example:

    docker run --rm node-express
    docker run --rm --runtime=runnc node-express-nabla

### Modifying Dockerfiles

In the general case, each `Dockerfile.nabla` represents a stage build.
For example, the first stage may install all of the node.js or Python
packages necessary in a standard container, then the second stage
copies them into a fresh nabla base container for the language
runtime.

The example `Dockerfile.nabla` files in this repository assume that
the bases are available locally, as if built from the
[nabla-base-build](https://github.com/nabla-containers/nabla-base-build)
repository.  Alternatively, the `FROM` line could reference our base
images on [Docker hub](https://hub.docker.com/u/nablact/), for
example:

    FROM nablact/nabla-node-base

### Information about the demo applications

* `node-express`: runs a node express web server.  Access it on port
  8080; you should receive a text string "Nabla!".

* `node-webrepl`: runs a webrepl in node.  Access it on port 8081.

* `python-tornado`: runs a Python tornado web server.  Access it on
  port 5000, you should see some `x`s.

* `redis-test`: runs a Redis key/value store.  Access it on port 6379
  using e.g. the Redis CLI (you should see OK):

      redis-cli -h 172.17.0.2 -p 6379 set foo bar


### See Also

* [nabla-containers/runnc](https://github.com/nabla-containers/runnc)
* [nabla-containers/nabla-base-build](https://github.com/nabla-containers/nabla-base-build)

