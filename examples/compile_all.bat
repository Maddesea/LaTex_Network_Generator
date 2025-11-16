@echo off
REM Compile all example files (Windows batch script)
REM Usage: compile_all.bat [compiler]
REM Default compiler: pdflatex

setlocal enabledelayedexpansion

set COMPILER=%1
if "%COMPILER%"=="" set COMPILER=pdflatex

set ERROR_COUNT=0
set SUCCESS_COUNT=0

echo =====================================
echo Network Diagram Examples Compiler
echo =====================================
echo Using compiler: %COMPILER%
echo.

REM List of example files
set EXAMPLES=01_basic_network_colorschemes.tex 02_enterprise_gradients.tex 03_security_with_badges.tex 04_multicloud_architecture.tex 05_accessibility_patterns.tex 07_complete_demo.tex

set BEAMER_EXAMPLE=06_beamer_presentation.tex

REM Compile each example
for %%f in (%EXAMPLES%) do (
    if exist %%f (
        echo Compiling: %%f

        REM Run compiler twice for references
        %COMPILER% -interaction=nonstopmode %%f > %%~nf_compile.log 2>&1

        if !errorlevel! equ 0 (
            %COMPILER% -interaction=nonstopmode %%f >> %%~nf_compile.log 2>&1

            if !errorlevel! equ 0 (
                echo   [32m✓ SUCCESS[0m: %%~nf.pdf created
                set /a SUCCESS_COUNT+=1

                REM Clean up auxiliary files
                del /q %%~nf.aux %%~nf.log %%~nf.out %%~nf.nav %%~nf.snm %%~nf.toc %%~nf_compile.log 2>nul
            ) else (
                echo   [31m✗ FAILED[0m: Second pass failed
                echo   See %%~nf_compile.log for details
                set /a ERROR_COUNT+=1
            )
        ) else (
            echo   [31m✗ FAILED[0m: Compilation error
            echo   See %%~nf_compile.log for details
            set /a ERROR_COUNT+=1
        )

        echo.
    ) else (
        echo Warning: %%f not found, skipping
        echo.
    )
)

REM Compile Beamer presentation
if exist %BEAMER_EXAMPLE% (
    echo Compiling Beamer presentation: %BEAMER_EXAMPLE%

    %COMPILER% -interaction=nonstopmode %BEAMER_EXAMPLE% > %BEAMER_EXAMPLE:~0,-4%_compile.log 2>&1

    if !errorlevel! equ 0 (
        %COMPILER% -interaction=nonstopmode %BEAMER_EXAMPLE% >> %BEAMER_EXAMPLE:~0,-4%_compile.log 2>&1

        if !errorlevel! equ 0 (
            echo   [32m✓ SUCCESS[0m: %BEAMER_EXAMPLE:~0,-4%.pdf created
            set /a SUCCESS_COUNT+=1

            del /q %BEAMER_EXAMPLE:~0,-4%.aux %BEAMER_EXAMPLE:~0,-4%.log %BEAMER_EXAMPLE:~0,-4%.out %BEAMER_EXAMPLE:~0,-4%.nav %BEAMER_EXAMPLE:~0,-4%.snm %BEAMER_EXAMPLE:~0,-4%.toc %BEAMER_EXAMPLE:~0,-4%_compile.log 2>nul
        ) else (
            echo   [31m✗ FAILED[0m: Second pass failed
            set /a ERROR_COUNT+=1
        )
    ) else (
        echo   [31m✗ FAILED[0m: Compilation error
        set /a ERROR_COUNT+=1
    )

    echo.
)

REM Summary
echo =====================================
echo Compilation Summary
echo =====================================
echo Successful: %SUCCESS_COUNT%
echo Failed: %ERROR_COUNT%
echo.

if %ERROR_COUNT% equ 0 (
    echo [32m✓ All examples compiled successfully![0m
    exit /b 0
) else (
    echo [31m✗ Some examples failed to compile[0m
    echo   Check the *_compile.log files for details
    exit /b 1
)
