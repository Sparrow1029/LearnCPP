def Settings( **kwargs ):
    return {
        'flags': [ '-x', 'c++', '-pedantic-errors', '-Wall', '-Weffc++', 'Wsign-conversion', '-Werror', '-std=c++2a' ],
    }