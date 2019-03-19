FROM nablact/nabla-go-base:v0.3

COPY src/ /goapp/
WORKDIR /goapp

RUN go get -d ./...
RUN make -f Makefile.goapp

FROM scratch
COPY --from=0 /goapp/goapp.spt /goapp.nabla
ENTRYPOINT ["/goapp.nabla"]
