import unittest
import os
import StringIO
from package_manager import util


CHECKSUM_TXT = "1915adb697103d42655711e7b00a7dbe398a33d7719d6370c01001273010d069"

DEBIAN_JESSIE_OS_RELEASE = """PRETTY_NAME="Distroless"
NAME="Debian GNU/Linux"
ID="debian"
VERSION_ID="8"
VERSION="Debian GNU/Linux 8 (jessie)"
HOME_URL="https://github.com/GoogleCloudPlatform/distroless"
SUPPORT_URL="https://github.com/GoogleCloudPlatform/distroless/blob/master/README.md"
BUG_REPORT_URL="https://github.com/GoogleCloudPlatform/distroless/issues/new"
"""

DEBIAN_STRETCH_OS_RELEASE = """PRETTY_NAME="Distroless"
NAME="Debian GNU/Linux"
ID="debian"
VERSION_ID="9"
VERSION="Debian GNU/Linux 9 (stretch)"
HOME_URL="https://github.com/GoogleCloudPlatform/distroless"
SUPPORT_URL="https://github.com/GoogleCloudPlatform/distroless/blob/master/README.md"
BUG_REPORT_URL="https://github.com/GoogleCloudPlatform/distroless/issues/new"
"""

# VERSION and VERSION_ID aren't set on unknown distros
DEBIAN_UNKNOWN_OS_RELEASE = """PRETTY_NAME="Distroless"
NAME="Debian GNU/Linux"
ID="debian"
HOME_URL="https://github.com/GoogleCloudPlatform/distroless"
SUPPORT_URL="https://github.com/GoogleCloudPlatform/distroless/blob/master/README.md"
BUG_REPORT_URL="https://github.com/GoogleCloudPlatform/distroless/issues/new"
"""

osReleaseForDistro = {
    "jessie": DEBIAN_JESSIE_OS_RELEASE,
    "stretch": DEBIAN_STRETCH_OS_RELEASE,
    "???": DEBIAN_UNKNOWN_OS_RELEASE,
}

class TestUtil(unittest.TestCase):

    def test_sha256(self):
        current_dir = os.path.dirname(__file__)
        filename = os.path.join(current_dir, 'testdata', 'checksum.txt')
        actual = util.sha256_checksum(filename)
        self.assertEqual(CHECKSUM_TXT, actual)

    def test_generate_debian_os_release(self):
        for distro in ["jessie", "stretch", "???"]:
            output_file = StringIO.StringIO()
            util.generate_os_release(distro, output_file)
            self.assertEqual(osReleaseForDistro[distro], output_file.getvalue())

if __name__ == '__main__':
    unittest.main()
