import inspect, os, sys
import stringtree

print "StringTree Python Demo"
print "----------------------"

dr = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

dictionary = stringtree.Tree()

print "Loading Dictionary..."

f = open(dr+'/dictionary.txt', 'r')
c = 0
for ln in f:
  dictionary.add(ln.strip(), c)
  c += 1
f.close()

print "Loaded "+str(c)+" words."

# Partial Matching
print "-Partial Matching -----------------"
print "-Type 'exit' to quit"
while True:
  x = raw_input("> ")
  if x == "exit":
    break
  for i in dictionary.partials(x):
    sys.stdout.write(i+" ")
  print

