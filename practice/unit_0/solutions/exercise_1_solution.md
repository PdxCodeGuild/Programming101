# Unit 1 Practice Solutions

## Exercise 1

This solution was created using a Linux terminal. A terminal on a Mac OS will look similar. If you're on Windows, instead of 

    [myComputer Desktop]$

You may see something more like:

    C:\Users\currentUser\Desktop> 


### 1.1

**Solution**

Make sure the terminal is navigated on the `Desktop`

    [myComputer Desktop]$ 

If you type `ls`, you should see the contents of the `Desktop`.

If you are not on the `Desktop` or would like to place your `pdx_code` folder somewhere else, use `cd <DIRECTORY_NAME>` to change directory.

    [myComputer ~]$ ls
    Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos

    [myComputer ~]$ cd Desktop

    [myComputer Desktop]$

Once you've navigated to the desired directory, use the command `mkdir` to create a directory named `pdx_code`.

    [myComputer Desktop]$ mkdir pdx_code

    [myComputer Desktop]$ ls
    pdx_code

Now we can navigate into our `pdx_code` directory    

    [myComputer Desktop]$ cd pdx_code

    [myComputer pdx_code]$ 

Inside your folder, create a subdirectory (folder within a folder) for `programming_101` and a subdirectory called `extra`

    [myComputer pdx_code]$ mkdir programming_101 extra

Notice `mkdir` is only executed once, but multiple folders are created by separating their names with spaces

Now if we type `ls` we see our new directories

    [myComputer pdx_code]$ ls
    extra programming_101

Navigate into the `programming_101` directory

    [myComputer pdx_code]$ cd programming_101

    [myComputer programming_101]$

Inside the `programming_101` directory, create subdirectories for each of the five units for the course: `unit_1`, `unit_2`, `unit_3`, `unit_4` and `unit_5`. Type `ls` to see the new directories.

    [myComputer programming_101]$ mkdir unit_1 unit_2 unit_3 unit_4 unit_5

    [myComputer programming_101]$ ls 
    unit_1 unit_2 unit_3 unit_4 unit_5

Using `cd ..` navigate back up to the `pdx_code` folder. The `..` refers to the parent directory of the current directory

    [myComputer programming_101]$ cd ..

    [myComputer pdx_code]$


Create a `programming_102` directory. Create a subdirectory for each unit in Programming 102: `unit_1`, `unit_2`, `unit_3`, `unit_4` and `unit_5`

    [myComputer pdx_code]$ mkdir programming_102

    [myComputer pdx_code]$ ls
    extra programming_101 programming_102

    [myComputer pdx_code]$ cd programming_102

    [myComputer programming_102]$ mkdir unit_1 unit_2 unit_3 unit_4 unit_5

We actually don't need our `extra` folder. Navigate to the `pdx_code` folder using the terminal and delete it using `rm -rf <DIRECTORY_NAME>`.

    [myComputer programming_102]$ cd ..

    [myComputer pdx_code]$ ls
    extra programming_101 programming_102

    [myComputer programming_102]$ rm -rf extra

    [myComputer programming_102]$ ls
    programming_101 programming_102

## [< Exercise 1](../exercise_1.md)

### [<< Back to syllabus](/)