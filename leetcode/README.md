# leetcode

CLI app to download leetcode submissions

## Usage

```
usage: leetcode [-h] [-b BASE_URL] [-s SESSION] [-f SUBMISSIONS_FILE] [-d SUBMISSIONS_DIR] [-o OFFSET] [-l LIMIT] {download,generate,update}

positional arguments:
  {download,generate,update}
                        what action to take

options:
  -h, --help            show this help message and exit
  -b BASE_URL, --base-url BASE_URL
                        Leetcode base url with protocol (default: https://leetcode.com)
  -s SESSION, --session SESSION
                        Session cookie to download submissions (default: ${LEETCODE_SESSION})
  -f SUBMISSIONS_FILE, --submissions-file SUBMISSIONS_FILE
                        JSON file to write submissions to (default: submissions.json)
  -d SUBMISSIONS_DIR, --submissions-dir SUBMISSIONS_DIR
                        Directory to generate submissions in (default: submissions)
  -o OFFSET, --offset OFFSET
                        Offset of submissions downloads (default: 0)
  -l LIMIT, --limit LIMIT
                        Limit of submission downloads (default: 20)
```
