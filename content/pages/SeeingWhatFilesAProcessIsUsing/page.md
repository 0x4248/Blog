# Seeing what files a process is using in Linux
***
There are several ways to see what files a process is using in Linux:

- [Trough /proc filesystem](#trough-<code>/proc</code>-filesystem)
- [Using lsof](#using-<code>lsof</code>)
- [Using fuser](#using-<code>fuser</code>)

## Trough `/proc` filesystem

In linux the `/proc` filesystem is a virtual filesystem that provides a way to interact with the kernel and processes and retrieve information about running processes and kernel information. If you `cd` into `/proc` and `ls` you will see a list of directories with numbers as names.

```
cd /proc
ls -l
```

You should see a similar output to this:

```
total 0
dr-xr-xr-x  9 root             root                           0 May 26 18:33 1/
dr-xr-xr-x  9 root             root                           0 May 26 18:33 10/
dr-xr-xr-x  9 root             root                           0 May 26 18:33 1072/
<MORE OUTPUT>
dr-xr-xr-x  9 root             root                           0 May 26 18:33 49/
dr-xr-xr-x  9 root             root                           0 May 26 18:33 5/
dr-xr-xr-x  9 root             root                           0 May 26 18:33 50/
dr-xr-xr-x  9 root             root                           0 May 26 18:33 52/
dr-xr-xr-x  9 systemd-timesync systemd-timesync               0 May 26 18:33 524/
dr-xr-xr-x  9 root             root                           0 May 26 18:33 54/
dr-xr-xr-x  9 root             root                           0 May 26 18:33 546/
dr-xr-xr-x  9 root             root                           0 May 26 18:33 55/
<MORE OUTPUT>
dr-xr-xr-x  2 root             root                           0 May 26 18:33 acpi/
dr-xr-xr-x 13 root             root                           0 May 26 18:33 asound/
-r--r--r--  1 root             root                           0 May 26 19:07 buddyinfo
dr-xr-xr-x  4 root             root                           0 May 26 19:07 bus/
-r--r--r--  1 root             root                           0 May 26 18:33 cgroups
-r--r--r--  1 root             root                           0 May 26 18:33 cmdline
-r--r--r--  1 root             root                           0 May 26 19:07 consoles
-r--r--r--  1 root             root                           0 May 26 18:33 cpuinfo
-r--r--r--  1 root             root                           0 May 26 19:07 crypto
-r--r--r--  1 root             root                           0 May 26 18:33 devices
-r--r--r--  1 root             root                           0 May 26 18:33 diskstats
dr-xr-xr-x  3 root             root                           0 May 26 19:07 driver/
dr-xr-xr-x  3 root             root                           0 May 26 19:07 dynamic_debug/
-r--r--r--  1 root             root                           0 May 26 19:07 execdomains
-r--r--r--  1 root             root                           0 May 26 19:07 fb
-r--r--r--  1 root             root                           0 May 26 18:33 filesystems
dr-xr-xr-x  5 root             root                           0 May 26 19:07 fs/
-r--r--r--  1 root             root                           0 May 26 19:07 interrupts
-r--r--r--  1 root             root                           0 May 26 19:07 iomem
-r--r--r--  1 root             root                           0 May 26 19:07 ioports
dr-xr-xr-x 55 root             root                           0 May 26 19:07 irq/
-r--r--r--  1 root             root                           0 May 26 19:07 kallsyms
<MORE FILES BELOW>
```

Each number directory corresponds to a process running on the system. If you `cd` into one of these directories you will see a list of files that contain information about the process. Here you can see everything from the command line that started the process to the environment variables that the process is using. We are interested in the `fd` directory which contains the file descriptors that the process is using.

For a test lets spin up python and open a file:

```
touch test.txt
python3
```

Then on the prompt we type the following:

```
f = open('test.txt', 'w')
```

Now run `ps` to get the PID of the python process:

```
ps aux | grep python
```

You should see an output similar to this:

```
    5452 pts/1    S+     0:00 python3
    5576 pts/0    S+     0:00 grep --color=auto python
```

The PID of the python process is `5452`. This will be different on your system. Now `cd` into the `/proc` directory and `ls`:

```
cd /proc/<PID>
```

Now cd into the `fd` directory:

```
cd fd
```

Now `ls` to see the file descriptors that the process is using:

```
ls -l
```

You should see an output similar to this:

```
lrwx------ 1 admin admin 64 May 26 19:25 0 -> /dev/pts/1
lrwx------ 1 admin admin 64 May 26 19:25 1 -> /dev/pts/1
lrwx------ 1 admin admin 64 May 26 19:25 2 -> /dev/pts/1
l-wx------ 1 admin admin 64 May 26 19:25 3 -> /home/admin/test.txt
```

The file descriptor `3` is the file that we opened in python. You can see that the file descriptor is pointing to the file `test.txt`.

## Using `lsof`

`lsof` is a command that lists open files. You can use `lsof` to see what files a process is using. To see what files a process is using you can run the following command:

```
lsof -p <PID>
```

Using our same python example from before:

```
lsof -p 5452
```

You should see an output similar to this:

```
COMMAND  PID  USER   FD   TYPE DEVICE SIZE/OFF    NODE NAME
python3 5452 admin  cwd    DIR  254,2     4096 4718594 /home/admin
python3 5452 admin  rtd    DIR  254,2     4096       2 /
<MORE OUTPUT>
python3 5452 admin    0u   CHR  136,1      0t0       4 /dev/pts/1
python3 5452 admin    1u   CHR  136,1      0t0       4 /dev/pts/1
python3 5452 admin    2u   CHR  136,1      0t0       4 /dev/pts/1
python3 5452 admin    3w   REG  254,2        0 4771062 /home/admin/test.txt
```

You can see that the file `test.txt` is being used by the python process.

## Using `fuser`

`fuser` is a command that displays the PIDs of processes using the specified files or file systems. To see what files a process is using you can run the following command:

```
fuser -v <file>
```

Using our same python example from before:

```
fuser -v test.txt
```

You should see an output similar to this:

```
                     USER        PID ACCESS COMMAND
/home/admin/test.txt:
                     admin      5452 F.... python3
```

You can see that the file `test.txt` is being used by the python process.

---
## See also
- [The /proc filesystem - kernel.org](https://www.kernel.org/doc/html/latest/filesystems/proc.html)
- [proc(5) -  man7.org](https://www.man7.org/linux/man-pages/man5/proc.5.html)
- [lsof(8) - man7.org](https://www.man7.org/linux/man-pages/man8/lsof.8.html)
- [fuser(1) - man7.org](https://www.man7.org/linux/man-pages/man1/fuser.1.html)

## Read more
- [The linux file system - kernel.org](https://www.kernel.org/doc/html/latest/filesystems/index.html)
- [Linux File System Hierarchy - tldp.org](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/index.html)