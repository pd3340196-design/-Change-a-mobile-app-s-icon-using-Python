from jnius import autoclass, cast

def change_mobile_icon(enable_new_icon=True):
    # Fetch native Android classes
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    ComponentName = autoclass('android.content.ComponentName')
    PackageManager = autoclass('android.content.pm.PackageManager')
    
    current_activity = PythonActivity.mActivity
    package_manager = current_activity.getPackageManager()
    package_name = current_activity.getPackageName()
    
    # Define paths to our manifest activity aliases
    default_alias = ComponentName(package_name, f"{package_name}.MainActivityAliasDefault")
    new_alias = ComponentName(package_name, f"{package_name}.MainActivityAliasNew")
    
    if enable_new_icon:
        # Enable the new icon alias
        package_manager.setComponentEnabledSetting(
            new_alias,
            PackageManager.COMPONENT_ENABLED_STATE_ENABLED,
            PackageManager.DONT_KILL_APP
        )
        # Disable the old default icon alias
        package_manager.setComponentEnabledSetting(
            default_alias,
            PackageManager.COMPONENT_ENABLED_STATE_DISABLED,
            PackageManager.DONT_KILL_APP
        )
    else:
        # Revert back to the default icon
        package_manager.setComponentEnabledSetting(
            default_alias,
            PackageManager.COMPONENT_ENABLED_STATE_ENABLED,
            PackageManager.DONT_KILL_APP
        )
        package_manager.setComponentEnabledSetting(
            new_alias,
            PackageManager.COMPONENT_ENABLED_STATE_DISABLED,
            PackageManager.DONT_KILL_APP
        )
