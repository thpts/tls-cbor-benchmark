# TLS CBOR vs ASN.1 analysis

This repository is an attempt to build a benchmarking harness allowing for
reproducible testing of draft-raza-ace-cbor-certificates, which describes X.509
serialisation with CBOR instead of the de facto ASN.1.

## Structure

* `analysis` - Paper written in R Notebook that describes the research
* `collector` - Process that collects certificates from the Certificate
  Transparency logs
* `converter` - Tooling that converts ASN.1 certificates into CBOR 

## Building and running

You will need Docker present in order to generate any of the data yourself.

```bash

    # Build the Docker containers locally
    make build

    # Collect
    make collector

    # TODO: Steps to perform post collection

    # Generate the paper
    make analysis

```

## Licensing

Source code within this repository is licensed under the [Apache
2](http://www.apache.org/licenses/LICENSE-2.0) software license.

Prose and non-software is licensed under the [Creative Commons Attribution 2.0
Generic](https://creativecommons.org/licenses/by/2.0/) license. Referring to
this code repository on Github along with author's names is sufficient in order
to be compliant with attribution.
