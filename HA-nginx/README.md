# Requirements

 * vagrant
 * ansible
 * qemu-kvm


# Notice

By default, 3 VMs are created as NGINX webservers, and 2 VMs are created as HA proxy servers. If you want to change the number of instantiate VMs, you can change the loop interval in the Vagrantfile


Ex Instantiate 2 VMs thereas 3:
```
(1..2).each do |i|
      config.vm.define "web-#{i}" do |server|
          server.vm.box = "debian/bullseye64"
          server.vm.network :private_network, :ip => "10.10.0.#{i+1}", :libvirt__domain_name => "test.local"
          server.vm.hostname = "web-#{i}"
      end
  end
```


# How to launch ?

```
vagrant up
```