.PHONY: analysis-build analysis collector-build collector

build: analysis-build 

collector-build:
	docker build -t cbor-tls-collector collector/

collector:
	docker run --rm -v ${PWD}/data:/data cbor-tls-collector

analysis-build:
	docker build -t cbor-tls-analysis analysis/

analysis:
	docker run --rm -v ${PWD}/analysis:/analysis -v ${PWD}/data:/data cbor-tls-analysis
