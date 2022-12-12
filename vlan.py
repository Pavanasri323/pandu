---
- hosts: switches
  connection: local
  vars:
    vlan_id: 998
    vlan_name: Ansible_VLAN
	ansible.netcommon.network_cli
  tasks:
    - name: Configure VLAN ID
      ios_config:
        lines:
          - vlan {{ vlan_id }}

    - name: Configure VLAN Name
      ios_config:
        lines:
          - name {{ vlan_name }}
        parents: vlan {{ vlan_id }}

    - name: Show VLAN
      ios_command:
        commands: show vlan brief
      register: show_vlan

    - debug: var=show_vlan.stdout_lines
	
	127.0.0.1