# astrotk

**astrotk** is a high level astrodynamics tool-kit for swift analysis in all aspects of orbital mechanics, with
powerful kernels written in C++.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Currently there are no prerequisites outside of the Python packet manager PyPi. This will change if the user opts to 
use the simulation kernel of Tudat when this is included.
 
### Installing

Clone the repository from GitHub:

```bash
git clone https://github.com/ggarrett13/astrotk.git
```

Navigate to the repository folder::
```bash
cd /astrotk
```

Install `astrotk` and its dependencies:
```bash
pip3 install .
```
## Running the tests

```bash
pytest  # while in top-level directory
```

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* **Geoffrey Garrett** - *Initial work* - [ggarrett](https://github.com/ggarrett13)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* DominicDirkx [DominicDirkx](https://github.com/DominicDirkx)

