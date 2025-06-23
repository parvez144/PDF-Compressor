#define MyAppName "PDF Compressor"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Shahriar Parvez Khan"
#define MyAppExeName "PDF_Compressor_Setup.exe"

[Setup]
AppId={{spk-144-0001}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputDir=Output
OutputBaseFilename={#MyAppExeName}
Compression=lzma
SolidCompression=yes
WizardStyle=modern
SetupIconFile=spk.ico
UninstallDisplayIcon={app}\{#MyAppExeName}

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "dist\PDF_Compressor.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "spk.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\PDF_Compressor.exe"; IconFilename: "{app}\spk.ico"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\PDF_Compressor.exe"; IconFilename: "{app}\spk.ico"; Tasks: desktopicon

[Run]
Filename: "{app}\PDF_Compressor.exe"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent 
