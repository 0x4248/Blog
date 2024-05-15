# Linux from scratch (ARM64)

This is a tutorial on how to build linux from scratch 

## Dependencies

```bash
apt-get update
apt-get install -y git fakeroot build-essential ncurses-dev xz-utils libssl-dev bc flex libelf-dev bison cpio

apt-get install -y qemu-system-aarch64 vim nano
```

## Downloading the sources

We need to download the sources including the linux kernel and busybox.

```bash
cd ~
git clone https://www.github.com/torvalds/linux
git clone https://www.github.com/mirror/busybox
```

In future if the builds fail you can always re-download a stable version of the linux kernel from https://www.kernel.org/ and busybox from https://www.busybox.net/downloads/

## Building the linux kernel

Now we need to build the linux kernel. First we need to configure the kernel. Run the following commands:

```bash
cd ~/linux
make menuconfig
```

You can now configure the linux kernel to your needs. To save and exit press `esc` twice and press save.

```bash
make -j$(nproc)
```

**CHECK** Has there been a file created called `arch/arm64/boot/Image` if not then the build has failed and you need to check the error messages and fix them.

## Building busybox

Now we need to build busybox. First we need to configure busybox. Run the following commands:

```bash
cd ~/busybox
make defconfig
make menuconfig
```

**IMPORTANT STEP** In the busybox configuration we need to change the `Build static binary (no shared libs)` to `y` and then save the configuration. This configuration is stored in `settings>build options>build static binary (no shared libs)`.

Now we can build busybox:

```bash
make -j$(nproc)
```

Now we need to install busybox to our source directory:

```bash
make install
```

**CHECK** Has there been a folder created called `/busybox/_install`. This should contain the busybox binary's and the base initramfs. If not then the build has failed and you need to check the error messages and retry this step.


## Creating the initramfs

Now we need to create the initramfs. Run the following commands:

```bash
cd ~/busybox/_install
mkdir -p dev
mknod dev/console c 5 1
mknod dev/ram b 1 0
```

We now need to make a `init` script which will be the first thing that runs when we boot linux. Run the following command:

```bash
nano init
```

Or if you prefer vim:

```bash
vim init
```

This should put you in a text editor. Copy the following into it:

```bash
#!/bin/sh
mkdir /proc /sys /tmp
mount -t proc none /proc
mount -t sysfs none /sys
mount -t tmpfs none /tmp
echo "Welcome to LFS"

exec /bin/sh
```

Now we need to make the init script executable:

```bash
chmod a+x init
```

Now we need to make the initramfs:

```bash
find -print0 | cpio -0oH newc | gzip -9 > ~/initramfs.cpio.gz
```

Now open finder and go to your `Documents/busybox` folder and you should see a file called `initramfs.cpio.gz`. Drag it to your user folder and rename it to `initramfs.cpio.gz`. This will be important later on.

## Running the linux kernel

Now we have everything we need to run the linux kernel.

```bash
qemu-system-aarch64 -kernel ~/linux/arch/arm64/boot/Image -initrd ~/initramfs.cpio.gz \
  --append "root=/dev/ram rw init=/init.sh" -nographic \
  -machine virt \
  -cpu cortex-a57 \
  -m 2G \
```

This should boot linux and you should see the following:

```bash
Welcome to LFS
~ # 
```

Congratulations you have now successfully built linux and ran it from scratch.

---
## See also
- [Kernel.org](https://www.kernel.org/)
- [Linux from scratch](https://www.linuxfromscratch.org/)
- [Busybox](https://www.busybox.net/)
- [QEMU](https://www.qemu.org/)
- [Original tutorial from github](https://gist.github.com/0x4248/6e1499eb7a6d79349404780f14fdc38d)

## References
Thanks to the following references, without them this tutorial would not be possible:

- [Linux from scratch](https://www.linuxfromscratch.org/)
- [PhoenixNAP](https://phoenixnap.com/kb/build-linux-kernel)
- [iBug Blog](https://ibug.io/blog/2019/04/os-lab-1/)
- [Kernel docs](https://www.kernel.org/doc/html/latest/)


## Further reading
- [Kernel hacking guide (KernelNewbies)](https://kernelnewbies.org/KernelHacking)
- [Kernel hacking guide (Kernel.org)](https://www.kernel.org/doc/html/latest/kernel-hacking/index.html)
