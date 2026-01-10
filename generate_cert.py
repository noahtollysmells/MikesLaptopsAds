#!/usr/bin/env python3
"""Generate self-signed SSL certificate for sync server"""
import subprocess
import os
import sys

cert_file = "server.crt"
key_file = "server.key"

# Check if OpenSSL is available
try:
    result = subprocess.run(
        ["openssl", "req", "-x509", "-newkey", "rsa:2048", "-keyout", key_file, 
         "-out", cert_file, "-days", "365", "-nodes",
         "-subj", "/C=US/ST=State/L=City/O=Organization/CN=mlads.online"],
        capture_output=True,
        text=True,
        timeout=10
    )
    if result.returncode == 0:
        print(f"✓ Certificate generated successfully!")
        print(f"  Certificate: {cert_file}")
        print(f"  Private Key: {key_file}")
        sys.exit(0)
    else:
        print(f"Error: {result.stderr}")
        sys.exit(1)
except FileNotFoundError:
    print("OpenSSL not found. Trying alternative method...")
    # If OpenSSL is not available, try using Python's cryptography module
    try:
        from cryptography import x509
        from cryptography.x509.oid import NameOID
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.backends import default_backend
        from cryptography.hazmat.primitives.asymmetric import rsa
        from cryptography.hazmat.primitives import serialization
        import datetime
        
        # Generate private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        
        # Generate certificate
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"State"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, u"City"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Organization"),
            x509.NameAttribute(NameOID.COMMON_NAME, u"mlads.online"),
        ])
        
        cert = x509.CertificateBuilder().subject_name(
            subject
        ).issuer_name(
            issuer
        ).public_key(
            private_key.public_key()
        ).serial_number(
            x509.random_serial_number()
        ).not_valid_before(
            datetime.datetime.utcnow()
        ).not_valid_after(
            datetime.datetime.utcnow() + datetime.timedelta(days=365)
        ).add_extension(
            x509.SubjectAlternativeName([x509.DNSName(u"mlads.online")]),
            critical=False,
        ).sign(private_key, hashes.SHA256(), default_backend())
        
        # Write certificate
        with open(cert_file, "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))
        
        # Write private key
        with open(key_file, "wb") as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))
        
        print(f"✓ Certificate generated successfully!")
        print(f"  Certificate: {cert_file}")
        print(f"  Private Key: {key_file}")
        sys.exit(0)
    except ImportError:
        print("Neither OpenSSL nor cryptography module found.")
        print("Install cryptography: pip install cryptography")
        sys.exit(1)
