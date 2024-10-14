# Jatszoter

A playgrounds management service.

Main goal for this project is provide easy-to-deploy testing
environments though web-console with SSH, control plan and
access to containers (stacks) networks.

We are targeting to use clean `Docker`, `kind` and `VMs` for our
playgrounds in the future, so we have trying to implement
some plugins' compatibility.

Moreover, we are planing to implement testing scenarios support
for academic use.

## Roadmap

- [ ] **agent:**: basic agent with only one provider for run `Docker` pre-built
   containers (public). Allow access to containers via SSH.

- [ ] **server**: simple API for agents registration, with simple UI
   for shows registered agents. no auth.

- [ ] **agent**: registration on server, send stats: running containers,
   links to ssh-web console, additional info.

...
