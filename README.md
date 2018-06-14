After you build the images using the `Makefile`s in each directory, you can run the nabla containers like this:

```
docker run --rm --runtime=runnc node-webrepl-nabla
docker run --rm --runtime=runnc node-express-nabla
docker run --rm --runtime=runnc python-tornado-nabla
docker run --rm --runtime=runnc redis-test-nabla
```
