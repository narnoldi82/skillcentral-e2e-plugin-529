#!/bin/sh
# Broken on purpose for SkillCentral #529: a hard-coded (fake, not a real key) private key block.
cat > /tmp/e2e-key <<'KEY'
-----BEGIN OPENSSH PRIVATE KEY-----
this-is-not-a-real-key-skillcentral-e2e-529-fixture-only
-----END OPENSSH PRIVATE KEY-----
KEY
