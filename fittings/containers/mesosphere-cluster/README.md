# Mesosphere cluster, with 3 masters and 9 slaves

The objective of this use case is to deploy a large cluster of Mesosphere nodes at the [Managed Cloud Platform from Dimension Data](http://cloud.dimensiondata.com/eu/en/).
This is done with [plumbery](https://developer.dimensiondata.com/display/PLUM/Plumbery) and a template that is provided below.

Mesosphere is a system that combines a number of components to effectively manage server clustering and highly available deployments on top of an existing operating system layer. Unlike systems like CoreOS, Mesosphere is not a specialized operating system and is instead a set of packages.

In this guide, we will go over how to configure a highly available cluster in Mesosphere. This configuration will set us up with failover in case any of our master nodes go down as well as a pool of slave servers to handle the tasks that are scheduled.

We will be using Ubuntu 14.04 servers for this guide.

## Requirements for this use case

* Select a MCP location
* Add a Network Domain
* Add an Ethernet network
* Deploy 12 Ubuntu nodes -- 3 masters and 9 slaves
* Provide a lot of resources to each slave
* Monitor all nodes in the real-time dashboard provided by Dimension Data
* Assign a public IPv4 address to each master node
* Add address translation rules to ensure Internet connectivity with each master
* Add firewall rule to accept TCP traffic on ports 22, 5050 and 8080 to each master
* Update the operating system of each node
* Synchronise node clock of each node
* Install a new SSH key to secure remote communications
* Configure SSH to reject passwords and to prevent access from root account
* Update `etc/hosts` and `hostnames` to bind IPv6 addresses to host names
* Install Docker Engine at all servers
* Install Consul on the manager node to implement dynamic discovery back-end
* Run Docker Swarm Manager at the queen
* Run Docker Swarm at every other bee

## Fittings plan

[Click here to read fittings.yaml](fittings.yaml)

## Deployment command

    $ python -m plumbery fittings.yaml deploy

This command will build fittings as per the provided plan, start nodes
and bootstrap them. Look at messages displayed by plumbery while it is
working, so you can monitor what's happening.

## Follow-up commands

At the end of the deployment, plumbery will display on screen some instructions
to help you move forward. You can ask plumbery to display this information
at any time with the following command:

    $ python -m plumbery fittings.yaml information

In this use case you can use the IPv4 assigned to the manager for direct ssh
connection.

    $ ssh ubuntu@<ipv4_of_the_queen_here>

From there you will check both the status of the local Docker Engine, and the
status from the full Docker Swarm:

    $ docker info
    $ docker -H :4000 info

Next step is to run a new Redis container somewhere in the swarm:

    $ docker -H :4000 run --name some-redis -d redis

And, of course, you may want to identify which node is running redis
exactly:

    $ docker -H :4000 ps -l | grep redis


## Destruction commands

Launch following command to remove all resources involved in the fittings plan:

    $ python -m plumbery fittings.yaml dispose

## Use case status

- [x] Work as expected

## See also

- [Containers with plumbery](../)
- [All plumbery fittings plan](../../)

