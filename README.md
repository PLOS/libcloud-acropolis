# libcloud-acropolis

This is a compute driver allowing apache [libcloud](https://libcloud.apache.org/) to manage
the Nutanix [Acropolis Hypervisor](https://www.nutanix.com/products/acropolis/) (AHV).

In turn, it powers a salt-cloud driver, allowing easy provisioning of VMs through saltstack.

Until it is accepted in the upstream release of libcloud, you can install libcloud-acropolis
via pip, and
[register it](https://libcloud.readthedocs.io/en/latest/other/registering-a-third-party-driver.html)
for use in your project. For example:

```
from libcloud.compute.providers import get_driver
from libcloud.compute.providers import set_driver

set_driver('acropolis', 'libcloud_acropolis.compute.acropolis', 'AcropolisNodeDriver')
driver = get_driver('acropolis')
```

## acropolis api

Nutanix provides a Swagger interface and spec for the AHV API, but as of this writing, the API
spec they provide does not validate in pyswagger or swagger-codegen, so it appears to be
effectively useless.

Unfortunately that means that this library largely implements its REST client by forming individual
requests using the requests library.

## status

Unreleased. Not yet usable.

## upstream status

Review not yet requested.