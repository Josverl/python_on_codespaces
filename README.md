# Description

This is a quick demo of the use of codespaces in GitHub for workshop purposes.

all participants need a GH account ( can be free version ) 
this will give them access to the codespace feature on **public** repos 

- full and preconfigured VSCode , in browser or local 
- CPython or conda possible based on the underlying base image 
- Fast to starty ( Github hase a pool of preconfigured images, and very fast storage / network)
- You do need to take care to prevent secret sharing ( .gitignore, template .env files, etc) 
- saving state will happen to codespaces, no branch or fork needed per se 
- but if you want permanent changes can be done by creating a fork 
- It is possible to create a deeplink to create a code-space 
  - https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=883788287&skip_quickstart=false
 

| Account Plan                       | Storage per Month | Core Hours per Month |
|------------------------------------|-------------------|----------------------|
| GitHub Free for personal accounts  | 15 GB-month       | 120                  |

so with a 2-core machine you can run 60 hours of codespaces per month for free
with a 4 core machine you can run 30 hour of codespaces per month for free

https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces

# Also see 
This repository contains a collection of codespaces which can be used to demonstrate the
[feature](https://github.com/features/codespaces) at various levels, from a default codespace (i.e.,
with no configuration specified) to a complex one with full support for developing machine learning
applications using Python.

Each of the following branches can be used to showcase a different type of codespace:

- [default](https://github.com/dassencio/codespaces-demo-python/tree/default): No codespace
  configuration. This can be used to illustrate what a barebones codespace looks like and how it can
  be used to bootstrap more complex codespaces or to simply create and modify files using a more
  powerful tool than the default GitHub editor.
- [simple](https://github.com/dassencio/codespaces-demo-python/tree/simple): Basic, manually-crafted
  codespace which can be used to develop a simple Python application.
- [complex](https://github.com/dassencio/codespaces-demo-python/tree/complex):
  Complex codespace containing a large collection of libraries, modules and tools which together
  form an environment where a machine learning application can be developed with little to no
  initial setup effort needed.



Start with the [default](https://github.com/dassencio/codespaces-demo-python/tree/default) branch,
then proceed to [simple](https://github.com/dassencio/codespaces-demo-python/tree/simple), then
finally [complex](https://github.com/dassencio/codespaces-demo-python/tree/complex). Each branch
will contain a `README.md` with further instructions.