import random
import hashlib
def sjs():
    a = random.randint(0, 100)
    a = "a" + str(a);
    b = random.randint(100, 10000);
    b = "b" + str(b);
    c = hashlib.md5(a.encode(encoding='UTF-8')).hexdigest() + hashlib.md5(b.encode(encoding='UTF-8')).hexdigest();
    c = "c" + str(c);
    d = random.randint(10, 100);
    d = "d" + str(d);
    e = hashlib.md5(c.encode(encoding='UTF-8')).hexdigest() + hashlib.md5(d.encode(encoding='UTF-8')).hexdigest();
    e = hashlib.md5(e.encode(encoding='UTF-8')).hexdigest()
    return e;