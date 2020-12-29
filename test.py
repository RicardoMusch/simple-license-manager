import os

cmdlist = ["python", "-m", "slm", "-check", "-licenserepo:'/home/Ricardo/Documents/GitHub/simple-license-manager/tests/license_repo'", "-env:SUBSTANCE_PAINTER_LICENSE"]
cmdlist = ["python", "-m", "slm", "-get", "-licenserepo:'/home/Ricardo/Documents/GitHub/simple-license-manager/tests/license_repo2'", "-env:SUBSTANCE_PAINTER_LICENSE"]
cmdlist = ["python", "-m", "slm", "-get", "-licenserepo:'/home/Ricardo/Documents/GitHub/simple-license-manager/tests/license_repo'", "-env:SUBSTANCE_PAINTER_LICENSE"]
cmdlist = ["python", "-m", "slm", "-reset", "-licenserepo:'/home/Ricardo/Documents/GitHub/simple-license-manager/tests/license_repo'", "-env:SUBSTANCE_PAINTER_LICENSE"]


os.system(" ".join(cmdlist))


