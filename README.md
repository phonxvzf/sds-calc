# sds-calc
A distributed integer calculator

## Installation
See [installation guide](https://github.com/phonxvzf/sds-calc/tree/master/install)

## HTTP Endpoints
### app-add
#### Synopsis
```
GET http://app-add:5001/<lhs>/<rhs>/<n>
GET http://<LOAD_BALANCER_IP>:30000/<lhs>/<rhs>/<n>
```
#### Returns
`rhs + lhs * n` (No multiplication is involved.)
#### Depends on
- None

--------

### app-diff
#### Synopsis
```
GET http://app-diff:5002/<lhs>/<rhs>/<n>
GET http://<LOAD_BALANCER_IP>:30001/<lhs>/<rhs>/<n>
```
#### Returns
`rhs - lhs * n` (No multiplication is involved.)
#### Depends on
- app-add

--------

### app-mult
#### Synopsis
```
GET http://app-mult:5003/<lhs>/<rhs>
GET http://<LOAD_BALANCER_IP>:30002/<lhs>/<rhs>
```
#### Returns
`lhs * rhs`
#### Depends on
- app-add

--------

### app-div
#### Synopsis
```
GET http://app-div:5004/<lhs>/<rhs>
GET http://<LOAD_BALANCER_IP>:30003/<lhs>/<rhs>
```
#### Returns
`lhs is 0 ? inf : floor(lhs / rhs)`
#### Depends on
- app-diff

