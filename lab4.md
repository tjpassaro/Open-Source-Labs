# Lab 4
## Open Source Patch Fix

### The Change
I fixed a minor grammatical error in the handbook section 8.2. The sentence hs slightly different meaning based on whether "and" or "or" is used. After reading the section many times over I concluded that "and" was actually the correct choice of word and a fix was necessary.

### Importance of Good Documentation
Good documentation is important in all code but most important in open source projects. In order to increase contribution to a project, possible contributers must be able to understand the code which is only possible with good documentation. In addition to losing support, bad documentation can lead to misunderstandings about the intention of the code, causing bad patches and bug prone updates. 

### Diff file
Index: /Users/thomaspassaro/Documents/chapter.xml
===================================================================
--- /Users/thomaspassaro/Documents/chapter.xml	(revision 49438)
+++ /Users/thomaspassaro/Documents/chapter.xml	(working copy)
@@ -86,7 +86,7 @@
     <para>Today, most of the functionality in the &os; kernel is
       contained in modules which can be dynamically loaded and
       unloaded from the kernel as necessary.  This allows the running
-      kernel to adapt immediately to new hardware or for new
+      kernel to adapt immediately to new hardware and for new
       functionality to be brought into the kernel.  This is known as
       a modular kernel.</para>
 
### Link to commit request
https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=213126
