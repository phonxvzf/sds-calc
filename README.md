# sds-calc
A distributed integer calculator

## Installation
See [installation section](https://github.com/phonxvzf/sds-calc/tree/master/install)

## HTTP Endpoints
### app-add
#### Synopsis
```
GET http://app-add/<rhs>/<lhs>/<n>
```
#### Returns
`rhs + lhs * n` (No multiplication is involved.)
#### Depends on
- None

--------

### app-diff
#### Synopsis
```
GET http://app-diff/<rhs>/<lhs>/<n>
```
#### Returns
`rhs - lhs * n` (No multiplication is involved.)
#### Depends on
- app-add

--------

### app-mult
#### Synopsis
```
GET http://app-mult/<rhs>/<lhs>
```
#### Returns
`rhs * lhs`
#### Depends on
- app-add

--------

### app-div
#### Synopsis
```
GET http://app-div/<rhs>/<lhs>
```
#### Returns
`lhs is 0 ? inf : floor(rhs / lhs)`
#### Depends on
- app-diff

