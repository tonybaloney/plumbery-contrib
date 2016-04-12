# Multiple network interfaces

The objective of this use case is to deploy a server with multiple network interfaces, at the [Managed Cloud Platform from Dimension Data](http://cloud.dimensiondata.com/eu/en/).
This is done with [plumbery](https://developer.dimensiondata.com/display/PLUM/Plumbery) and a template that is provided below.

## Requirements for this use case

* Select a MCP location
* Add a Network Domain
* Add 3 Ethernet networks: PrimaryNetwork, SecondaryNetwork and TertiaryNetwork
* Deploy a Ubuntu node
* Monitor this server in the real-time dashboard provided by Dimension Data
* Set the private IPv4 addresses on PrimaryNetwork and on TertiaryNetwork with fixed values
* Assign a public IPv4 address
* Add address translation to ensure end-to-end IP connectivity
* Add firewall rule to accept TCP traffic on port 22 (ssh)
* Update the operating system
* Synchronise node clock with NTP
* Install a new SSH key to secure remote communications
* Configure SSH to reject passwords and to prevent access from root account

## Fittings plan

[Click here to read fittings.yaml](fittings.yaml)

## Deployment command

    $ python -m plumbery fittings.yaml deploy

This command will build fittings as per the provided plan, start the server
and bootstrap it. Look at messages displayed by plumbery while it is
working, so you can monitor what's happening.

## Follow-up commands

At the end of the deployment, plumbery will display on screen some instructions
to help you move forward. You can ask plumbery to display this information
at any time with the following command:

    $ python -m plumbery fittings.yaml information

In this use case you can use the IPv4 assigned to the node for direct ssh
connection.

    $ ssh ubuntu@<ipv4_here>

You will have to accept the new host, and authentication will be based on
the SSH key communicated to the node by Plumbery.

    $ ifconfig

These commands are self-explanatory and validate networks deployment and configuration.

## Destruction commands

Launch following command to remove all resources involved in the fittings plan:

    $ python -m plumbery fittings.yaml dispose

## Use case status

- [ ] Work as expected

## See also

- [Example configurations with plumbery](../)
- [All plumbery fittings plans](../../)

