#!/usr/bin/env python3

from base64 import b64decode
from pyasn1.codec.der.decoder import decode as der_decoder
from pyasn1_modules.rfc5280 import Certificate

import logging
from base64 import b64decode
from argparse import ArgumentParser, RawTextHelpFormatter, ArgumentTypeError
import os

HELP="""
This script takes in a DER-encoded X.509 TLS certificates (otherwise might be
known as a PEM certificate) contained within a directory and outputs the same
files for analysis into a different folder with CBOR encoding. We assume that
all files are valid, encoded certificates and that no subfolders are present.
File names are preserved, however extensions are normalised to '.cbor'.
"""


def valid_dir(directory):
    """ Check the directory provided in an argument exists
    :param directory:
    """
    if not os.path.isdir(directory):
        raise ArgumentParser('"{}" appears invalid!'.format(directory))
    return directory


def convert_file(input_dir, cert_file, output_dir):
    """
    Convert a Base64 encoded, DER serialised X.509 certificate into a CBOR
    representation.

    The input file MUST NOT have PEM style headers (e.g "---- BEGIN ...") at the
    start nor end of the file.
    :param input_dir: Path certificates reside in
    :param cert_file: Path to the certificate to read
    :param output_dir: Path to write converted file to
    """
    with open(input_dir + cert_file, 'r') as der_file:
        b64_cert = der_file.read()

    try:
        der_cert = b64decode(b64_cert)
        asn1_cert, rest_of_data = der_decoder(der_cert, asn1Spec=Certificate())
    except Exception as err:
        logging.warn("Unable to read {}, skipping...".format(cert_file))
        return False
    logging.debug(asn1_cert.prettyPrint())


def main():
    logging.basicConfig(format='%(asctime)s %(message)s',
                        datefmt='%Y-%m-%dT%H:%M:%S%z')

    parser = ArgumentParser(description=HELP, formatter_class=RawTextHelpFormatter)

    parser.add_argument('--input-dir', dest='input_dir', action='store',
                        help='Input directory', type=valid_dir, required=True)
    parser.add_argument('--output-dir', dest='output_dir', action='store',
                        help='Output directory', type=valid_dir, required=True)

    args = parser.parse_args()

    logging.info('Converting files in {}...'.format(args.input_dir))

    for cert_file in os.listdir(args.input_dir):
        convert_file(args.input_dir, cert_file, args.output_dir)

    logging.info('Conversion complete!')
 
