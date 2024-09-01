#cftrace
Perform traceroute from the Cloudflare Network to various targets.

Inspired by https://github.com/jacobbednarz/cf-traceroute
Using https://github.com/gabanz/cf-looking-glass as the data source.

Corrections welcome

## Example
```
./python3 cftrace.py -targets ftp.is.co.za,mirror.ac.za -colos cpt01,jnb01
cpt01:
  ftp.is.co.za
   1   8.35.59.1 (8.35.59.1)                                        1.17ms (1.10~1.29, count=5)
   2   197.157.64.174 (197.157.64.174)                              0.27ms (0.20~0.35, count=5)
   3   196-60-70-126.ixp.capetown (196.60.70.126)                   3.19ms (1.19~3.72, count=5)
   4   168.209.2.17 (168.209.2.17)                                  0.77ms (0.63~0.95, count=5)
   5   mi-za-pkl-br3-ge0-0-0-12-510.ip.ddii.network (168.209.120.5) 17.20ms (16.23~18.70, count=5)
   6   168.209.120.2 (168.209.120.2)                                18.55ms (18.09~20.30, count=5)
   7   is-ops-pkl.fw.ip.ddii.network (196.34.7.196)                 17.82ms (17.34~18.12, count=5)
   8   ftp.dimensiondata.com (196.4.160.12)                         19.45ms (18.86~19.63, count=5)
  mirror.ac.za
   1   8.35.59.1 (8.35.59.1)                                        1.14ms (0.68~1.30, count=5)
   2   196.10.140.67 (196.10.140.67)                                20.86ms (20.83~20.89, count=5)
   3   lt-1-1-0-0-cpt3-pe1.net.tenet.ac.za (155.232.64.90)          5.04ms (0.62~7.87, count=5)
   4   et-1-1-0-0-cpt1-ir1.net.tenet.ac.za (155.232.64.86)          0.58ms (0.54~0.65, count=5)
   5   mirror-cpt-01.mirror.ac.za (155.232.191.55)                  0.86ms (0.63~0.99, count=5)
jnb01:
  ftp.is.co.za
   1   8.36.216.1 (8.36.216.1)                                      0.53ms (0.48~0.57, count=5)
   2   197.234.240.20 (197.234.240.20)                              14.12ms (0.77~22.92, count=5)
   3   206.249.2.97 (206.249.2.97)                                  0.92ms (0.81~1.05, count=5)
   4   be4429.ccr41.lon13.atlas.cogentco.com (154.54.5.34)          158.36ms (158.25~158.41, count=5)
   5   be2572.ccr21.lon02.atlas.cogentco.com (154.54.61.254)        158.70ms (158.64~158.77, count=5)
   6   149.6.148.130 (149.6.148.130)                                161.67ms (160.01~163.09, count=5)
   7   core2b-pkl-pos-0-7-5-0.ip.ddii.network (168.209.201.94)      169.36ms (166.97~173.03, count=5)
   8   mi-za-pkl-br3-ge0-0-0-12-510.ip.ddii.network (168.209.120.5) 171.65ms (168.93~173.40, count=5)
   9   168.209.120.2 (168.209.120.2)                                173.65ms (173.29~174.05, count=5)
  10   is-ops-pkl.fw.ip.ddii.network (196.34.7.196)                 171.62ms (166.35~173.43, count=5)
  11   ftp.dimensiondata.com (196.4.160.12)                         170.43ms (167.90~174.31, count=5)
  mirror.ac.za
   1   8.36.216.1 (8.36.216.1)                                      1.02ms (0.98~1.07, count=5)
   2   197.234.240.22 (197.234.240.22)                              2.99ms (0.78~5.99, count=5)
   3   tenet.jinx.net.za (196.60.96.33)                             0.45ms (0.38~0.52, count=5)
   4   lt-1-1-0-0-isd1-pe1.net.tenet.ac.za (155.232.128.77)         0.63ms (0.49~0.79, count=5)
   5   et-1-1-4-0-cpt3-pe1.net.tenet.ac.za (155.232.1.148)          16.54ms (16.23~16.65, count=5)
   6   et-1-1-0-0-cpt1-ir1.net.tenet.ac.za (155.232.64.86)          16.31ms (16.24~16.37, count=5)
   7   mirror-cpt-01.mirror.ac.za (155.232.191.55)                  16.29ms (16.18~16.34, count=5)
```

### DISCLAIMER:
This project is still experimental, so reliability cannot be guaranteed, especially in production environments. Proceed at your own risk! It works great for me... but YMMV - proceed at own risk.

### Donate
Did this make you happy? I'd love to do more development like this! Please donate to show your support :)

BTC: 1Q4QkBn2Rx4hxFBgHEwRJXYHJjtfusnYfy

XMR: 4AfeGxGR4JqDxwVGWPTZHtX5QnQ3dTzwzMWLBFvysa6FTpTbz8Juqs25XuysVfowQoSYGdMESqnvrEQ969nR9Q7mEgpA5Zm
