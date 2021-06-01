from subprocess import Popen, PIPE

    

proc = Popen(["python", "--version"], stdout=PIPE, stderr=PIPE)

(stdout, _) = proc.communicate()

print(stdout, _)

