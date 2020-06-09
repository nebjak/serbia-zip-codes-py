# Serbia zip codes

Easy access to Serbia zip codes. You can search zip code by city, or city by zip code.

## Installation

```
pip install serbia-zip-codes
```

## Usage

```python
from serbia_zip_codes import SerbiaZipCodes
```

Search city by city:

```python
result = SerbiaZipCodes.find_by_city("loznica")
print(result)
# >>> [ { city: 'Loznica', zip_code: '15300' } ]
print(result[0].zip_code)
# >>> 15300
```

Search city by zip code:

```python
result = SerbiaZipCodes.find_by_zip("15300")
print(result)
# prints
# [ { city: 'Loznica', zip_code: '15300' } ]
print(result[0].city)
# prints
# Loznica
```

Multiple results example:

```python
result = SerbiaZipCodes.find_by_city("beograd")
print(result)
# prints
# [ { city: 'Beograd', zip_code: '11000' },
#   { city: 'Beograd Vozdovac', zip_code: '11010' },
#   { city: 'Beograd Čukarica', zip_code: '11030' },
#   { city: 'Beograd Zvezdara', zip_code: '11050' },
#   { city: 'Beograd Palilula', zip_code: '11060' },
#   { city: 'Novi Beograd', zip_code: '11070' },
#   { city: 'Beograd Zemun', zip_code: '11080' },
#   { city: 'Beograd Rakovica', zip_code: '11090' },
#   { city: 'Mali Beograd', zip_code: '24309' } ]
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
