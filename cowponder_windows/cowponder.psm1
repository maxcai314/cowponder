#
#  Cowponder
#  a silly little funny
#
#  Copyright (c) 2023 Reid Dye
#  https://github.com/maxcai314/cowsay
# 
#  Based on John Kane's posh-cowsay:
#  https://github.com/kanej/posh-cowsay
#  
#  Which was based on Tony Monroe's cowsay: 
#  http://www.nog.net/~tony/warez/cowsay-3.03.tar.gz
#
#  Licensed under the GNU GPL version 3.0
#

#requires -Version 2.0

# cowponder Version
# $version = "0.0.2"

# Max Width of the Speech Bubble
$bubbleWidth = 40

# The different modes that are supported
$modes = @{
  "-b"= @("==", ' ') # Borg
  "-d"= @("XX", 'U') # Dead
  "-g"= @('$$', ' ') # Greedy
  "-p"= @("@@", ' ') # Paranoid
  "-s"= @("**", 'U') # Stoned
  "-y"= @("..", ' ') # Youthful
}

# Public

<# 
.Synopsis
  a rather pensive cow
.Description
  cowponder generates an ASCII art picture of a cow thinking some
  fascinating random thoughts. It word-wraps the message at about 40
  columns, and prints the cow saying the given message on standard
  output.

  cowponder also includes ponder, which provides the same functionality
  but without the bovine centerpiece so users may pipe the thoughts to
  their contemplative creature of choice.

  Different modes can be enabled by passing the appropriate option.
  For instance -d will enable Dead mode, were the cow shown appears
  to be dead. The complete list of options are:

    Borg     -b
    Dead     -d
    Greedy   -g
    Paranoid -p
    Stoned   -s
    Youthful -y

  Outside of the cow modes, there are several additional options. 
  Note that these are not available for ponder, since the ponder
  is the same software as cowponder and shares a thoughtbook.
    --version, -v         Display the version of cowponder and exit.
    --update,  -u         Update the thoughtbook from the interwebs.
                          This *will* erase any changes you've made; 
                          back up anything you want to keep!
    --add, -a [thought]   Add [thought] to the thoughtbook.
.Link
  https://github.com/maxcai314/cowponder
#>
function cowponder() {
  $params

  $messageArgs = @()
  $eyes = "oo"
  $tongue = " "
  $idx = 0
  if (-not(Test-Path -Path "$HOME\.cowthoughts" -PathType Leaf)) {
    Write-Output "moo moo; couldn't find thougtbook. downloading now."
    Invoke-WebRequest -Uri https://max.xz.ax/cowponder/cowthoughts.txt -OutFile $HOME\.cowthoughts
  }
  foreach($arg in $args) {

    if($arg -eq "-v" -or $arg -eq "--version") {
      Print-Version
      return
    }

    if($arg -eq "-u" -or $arg -eq "--update"){
      Invoke-WebRequest -Uri https://max.xz.ax/cowponder/cowthoughts.txt -OutFile $HOME\.cowthoughts
      return
    }

    if($arg -eq "-a" -or $arg -eq "--add") {
      Add-Content $HOME\.cowthoughts ($args[($idx + 1)..($args.Length - 1)] -join ' ')
      Write-Output ('Added "' + ($args[($idx + 1)..($args.Length - 1)] -join ' ') + '" to the thoughtbook!')
      return
    }

    if($modes.keys -contains $arg) {
      $eyes   = $modes[$arg][0]
      $tongue = $modes[$arg][1]
      continue
    }



  }
  $message = (Get-Random -InputObject (get-content $HOME\.cowthoughts))

  Print-MessageBubble($message) 

  Print-Cow $eyes $tongue
}
function Ponder() {
  if (-not(Test-Path -Path "$HOME\.cowthoughts" -PathType Leaf)) {
    Write-Output "moo moo; couldn't find thougtbook. downloading now."
    Invoke-WebRequest -Uri https://max.xz.ax/cowponder/cowthoughts.txt -OutFile $HOME\.cowthoughts
  }
  Write-Output (Get-Random -InputObject (get-content $HOME\.cowthoughts))
}

# Private

function Print-MessageBubble($message) {
  $lines = Convert-MessageToLines($message)
  $lineWidth = Max-Width($lines)

  Write-MessageBubbleBoundaryLine -lineWidth $lineWidth -boundaryChar '_' 

  foreach ($index in 0..($lines.length - 1)) {
    $delimiters = '()'
    $paddedLine = ' ' + $lines[$index] + ' '
    Write-MessageBubbleLine -lineWidth $lineWidth -delimiters $delimiters -text $paddedLine
  }

  Write-MessageBubbleBoundaryLine -lineWidth $lineWidth -boundaryChar '-'
}

function Print-Cow($eyes="oo", $tongue=" ") {
  Write-Output "      o  ^__^             "
  Write-Output "       o ($eyes)\________    "
  Write-Output "         (__)\        )\/\"
  Write-Output "          $tongue   ||----w |   "
  Write-Output "              ||     ||   "
}

function Print-Version() {
  Get-Package -n cowponder
}

# Helper Functions

function Convert-MessageToLines($message) {
  $words = Split-Message $message  
  $lines = @()
  $line = ""

  foreach($word in $words) {
    if(($line.length + $word.length + 1) -gt $bubbleWidth) {
      if($line -ne "") {
        $lines += ,$line
      }
      $line = $word 
    } else {
      if($line -eq "") {
        $line = $word
      } else {
        $line += " " + $word
      }
    }
  }

  $lastLine = $line

  $lines += ,$lastLine
  return ,$lines 
}

function Split-Message($message) {
  $wordsSplitOnSpaces = $message.split(" ")
  
  $words = [string[]]@()

  foreach($longWord in $wordsSplitOnSpaces) {
    $splitWords = Split-Word($longWord)
    foreach($word in $splitWords) {
      if($word -ne "") {
        $words+= ,[string]$word
      }
    }
  }

  return ,[string[]]$words
}

function Split-Word($word) {
  if($word.length -le $bubbleWidth) {
    return ,[string[]]@($word)
  }

  $splits = [string[]]@()

  foreach($i in (0..($word.length / $bubbleWidth))) {
    $startPoint = ($i * $bubbleWidth)
    if(($startPoint + $bubbleWidth) -gt $word.length) {
      $splits += $word.substring($startPoint)
    } else {
      $splits += $word.substring($startPoint, $bubbleWidth)
    }
  }

  return ,[string[]]$splits
}

function Max-Width($lines) {
  $maxLength = 0
  foreach($line in $lines) {
    if($line.length -gt $maxLength) {
      $maxLength = $line.length
    }
  }
  
  return $maxLength
}

function Write-MessageBubbleBoundaryLine($lineWidth, $boundaryChar) {
  Write-MessageBubbleLine -lineWidth $lineWidth `
                          -delimiters '  ' `
                          -text ("".padRight($lineWidth + 2, $boundaryChar))
}

function Write-MessageBubbleLine($lineWidth, $delimiters, $text) {
    $line = $delimiters[0] + ($text.padRight($lineWidth + 2, ' ')) + $delimiters[1]
    Write-Output $line.trimEnd()
}

# Exports
Export-ModuleMember cowponder
Export-ModuleMember ponder
