# versioned (Version Editor) - a version number tool

versioned (or versioned) is a simple command line tool to work with version 
numbers on the command line. Features include

- check if version number satisfies the version number format
- remove a "-SNAPSHOT" suffix
- calculate next release version
- calculate next snapshot version.

## Version number formats

versioned supports semantic versions of the form 1.2.3-SNAPSHOT for now. This
format is known from maven (a popular java build tool) and is called mvn.

```
versioned -f mvn -c isVersion foo
false
```

```
versioned -f mvn -c isVersion 1
true
```

```
versioned -f mvn -c isSnapshot 1-SNAPSHOT
true
```

```
versioned -f mvn -c isRelease 1-SNAPSHOT
false
```

```
versioned -f mvn -c nextRelease 1.2.3-SNAPSHOT
1.2.3
```

```
versioned -f mvn -c nextSnapshot 1.2.3-SNAPSHOT
1.2.4-SNAPSHOT
```

## License

MIT License

Copyright (c) 2016 Cornelius Buschka

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
