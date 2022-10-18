from subprocess import *


def jarWrapper(*args):
    process = Popen(['java', '-jar']+list(args), stdout=PIPE, stderr=PIPE)
    ret = []
    while process.poll() is None:
        line = process.stdout.readline()
        print(line)
        #if line != '' and line.endswith("\n"):
            #ret.append(line[:-1])
    stdout, stderr = process.communicate()
    #ret += stdout.split(r"\n")
    ret += stdout
    if stderr != '':
        #ret += stderr.split(r"\n")
        ret +=stderr
        return ret, False
    else:
        return ret, True
    
    


if __name__ == '__main__':
    
    args = ['myJarFile.jar', 'arg1', 'arg2', 'argN'] # Any number of args to be passed to the jar file

    result = jarWrapper(*args)

    print(result)