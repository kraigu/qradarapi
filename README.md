Waterloo's implementation of QRadar API calls.

Ideally python2/3 compatible.

Rationale
---------

https://github.com/ibm-security-intelligence/api-samples is fairly hostile to being used as a library, it's mostly just reference code. It also currently requires Python 3.3, which isn't as friendly as it could be.

Goal: provide at least some of the basic QRadar API functionality in a library that can be easily used by other Python applications.

Requirements
------------

A .qrrc file (this only works on *nix-type OSes) containing:

```
[info]
hostname = (name of your QRadar server)
apikey = (API key you generate at Admin | (User Management) | Authorized Services)
certbundlefile = (path to a certificate bundle file so we can avoid SSL errors on intranetssl certs)
```

TODO
----

Error checking, where it exists, is rudimentary at best. Debug logging should be done with logging module, not uncommenting print lines.

License
-------

BSD-new

Author
------

* Mike Patterson UWaterloo IST-ISS <mike.patterson@uwaterloo.ca>
