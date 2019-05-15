.PHONY: analysis-build analysis

build: analysis-build 

analysis-build:
	docker build -t cbor-tls-analysis analysis/

analysis:
	docker run --rm -v ${PWD}/analysis:/analysis -v ${PWD}/data:/data cbor-tls-analysis
