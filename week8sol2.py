def simplify_path(path):
    parts = path.split('/')
    stack = []

    for part in parts:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return '/' + '/'.join(stack)
print(simplify_path("/home/"))                
print(simplify_path("/a/./b/../../c/"))      
print(simplify_path("/../"))                  
print(simplify_path("/home//foo/"))           
print(simplify_path("/a/..//b/./c/../"))      
