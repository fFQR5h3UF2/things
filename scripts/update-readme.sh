#!/usr/bin/env bash
set -Eeuxo pipefail

usage_text="\
<!-- start usage -->

\`\`\`bash
$(tail -n +4 <./scripts/usage.sh)
\`\`\`

<!-- end usage -->\
"
usage_pattern='
/<!--.*usage.*-->/ { if (start) { end = 1 } else { print usage_text; start = 1 }; next }
!start || end { print }
'
awk -v usage_text="${usage_text}" "${usage_pattern}" README.md >README.new.md
if [[ ! -s "README.new.md" ]]; then
    echo "new readme is empty"
    exit 1
fi
mv README.new.md README.md
