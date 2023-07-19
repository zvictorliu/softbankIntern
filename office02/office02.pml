<?xml version="1.0" encoding="UTF-8" ?>
<Package name="office02" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="test" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="dance" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="main" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="take_pic" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="command" src="command/command.dlg" />
        <Dialog name="photo_taking" src="photo_taking/photo_taking.dlg" />
    </Dialogs>
    <Resources>
        <File name="main" src="html/main.html" />
        <File name="avatar" src="html/images/avatar.png" />
        <File name="ChatGPT_logo" src="html/images/ChatGPT_logo.png" />
        <File name="jquery-2.1.3.min" src="html/scripts/jquery-2.1.3.min.js" />
        <File name="jquery.easing.1.3" src="html/scripts/jquery.easing.1.3.js" />
        <File name="jquery.qimhelpers" src="html/scripts/jquery.qimhelpers.js" />
        <File name="main" src="html/scripts/main.js" />
        <File name="qimessaging" src="html/scripts/qimessaging.js" />
        <File name="socket.io.min" src="html/scripts/socket.io.min.js" />
    </Resources>
    <Topics>
        <Topic name="command_mnc" src="command/command_mnc.top" topicName="command" language="zh_CN" />
        <Topic name="photo_taking_mnc" src="photo_taking/photo_taking_mnc.top" topicName="photo_taking" language="zh_CN" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
        <Translation name="translation_zh_CN" src="translations/translation_zh_CN.ts" language="zh_CN" />
    </Translations>
</Package>
