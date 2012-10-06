on Run(f)
    set fl to posix file f as alias
    tell application "iTunes"
        add fl
    end tell
end run