# Tech Versus Me API

> *A RESTful JSON API for techversus.me built with Django REST Framework*

### Table of Contents

* [Introduction](#introduction)
* [Endpoints](#endpoints)
* [License](#license)

### Introduction

**REST** is an architecture style for designing networked applications and APIs over HTTP.
It stands for **RE**presentational **S**tate **T**ransfer.  
Web Services that conform to the REST architectural style, or RESTful web services, provide interoperability between computer systems on the Internet.

#### REST Constraints

As REST creator, Roy Fielding describes in his [doctoral dissertation](http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm), it was conceived as a whole sets of needs, shaped by the constraints of the environment in which this system was going to be implemented.
Such constraints are:

* Client-Server architecture
* Uniform Interface (Resource [URIs](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier), [Hypermedia](https://en.wikipedia.org/wiki/HATEOAS))
* Stateless
* Cacheable
* Layered System
* Code on demand (optional)

### Endpoints

| Name | URI | Method | Description |
| ----- | ----- | ----- | ----- |
| index | / | GET, OPTIONS | Index View with metadata |
| posts | /posts/ | GET, OPTIONS | List all posts |
| post | /posts/\<id:int>/ | GET, OPTIONS | Show individual post by id |
| authors | /authors/ | GET, OPTIONS | List all authors |
| author | /authors/\<id:int>/ | GET, OPTIONS | Show individual author by id |

### License

This code has been released under the [GNU General Public License v3.0](LICENSE).
