# Elastic Cloud Storage (ECS) from EMC, providing S3-like storage

The objective of this use case is to deploy a cluster of EMC ECS nodes at the [Managed Cloud Platform from Dimension Data](http://cloud.dimensiondata.com/eu/en/).
This is done with [plumbery](https://developer.dimensiondata.com/display/PLUM/Plumbery) and a template that is provided below.

![Architecture](architecture.png)

The cluster is built out of EMC ECS nodes. Resources assigned to each node can be changed by passing parameters to plumbery.

## Requirements for this use case

* Select a MCP location
* Add a Network Domain
* Add an Ethernet network
* Deploy 9 Ubuntu nodes
* Provide different CPU and RAM capacity depending on node role
* Monitor all nodes in the real-time dashboard provided by Dimension Data
* Assign a public IPv4 address to each node
* Add address translation rules to ensure Internet connectivity with each server
* Add firewall rule to accept TCP traffic on ssh to each node
* Update the operating system of each node
* Synchronise node clock of each node
* Install a new SSH key to secure remote communications
* Configure SSH to reject passwords and to prevent access from root account
* Update `etc/hosts` and `hostnames` to bind IPv6 addresses to host names
* Install ceph-deploy at the `admin` node
* Use ceph-deploy to deploy the full cluster

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

From there you will check both the status of the Ceph cluster:

    $ ceph health

## Destruction commands

Launch following command to remove all resources involved in the fittings plan:

    $ python -m plumbery fittings.yaml dispose

## Use case status

- [ ] Work as expected

## See also

- [Storage with plumbery](../)
- [All plumbery fittings plan](../../)

