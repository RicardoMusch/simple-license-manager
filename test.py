import os

cmdlist = ["python", "-m", "slm", "-check", "-licenserepo:'/home/Ricardo/Documents/GitHub/simple-license-manager/tests/license_repo'", "-env:SUBSTANCE_PAINTER_LICENSE"]
cmdlist = ["python", "-m", "slm", "-get", "-licenserepo:'/home/Ricardo/Documents/GitHub/simple-license-manager/tests/license_repo2'", "-env:SUBSTANCE_PAINTER_LICENSE"]
cmdlist = ["python", "-m", "slm", "-get", "-licenserepo:'/home/Ricardo/Documents/GitHub/simple-license-manager/tests/license_repo'", "-env:SUBSTANCE_PAINTER_LICENSE", "-exe:'C:/Program Files/Allegorithmic/Substance Painter/Substance Painter.exe'"]
#cmdlist = ["python", "-m", "slm", "-reset", "-licenserepo:'/home/Ricardo/Documents/GitHub/simple-license-manager/tests/license_repo'", "-env:SUBSTANCE_PAINTER_LICENSE"]


# Windows tests
cmdlist = ["python", "-m", "slm", "-get", "-licenserepo:'C:/Users/ricardom/Documents/github/simple-license-manager/tests/license_repo'", "-env:SUBSTANCE_PAINTER_LICENSE", "-exe:'C:/Program Files/Allegorithmic/Substance Painter/Substance Painter.exe'"]
#cmdlist = ["python", "-m", "slm", "-reset", "-licenserepo:'C:/Users/ricardom/Documents/github/simple-license-manager/tests/license_repo'", "-env:SUBSTANCE_PAINTER_LICENSE"]



os.system(" ".join(cmdlist))


