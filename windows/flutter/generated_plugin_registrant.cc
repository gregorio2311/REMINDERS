//
//  Generated file. Do not edit.
//

// clang-format off

#include "generated_plugin_registrant.h"

<<<<<<< Updated upstream
#include <desktop_webview_auth/desktop_webview_auth_plugin.h>
#include <firebase_core/firebase_core_plugin_c_api.h>

void RegisterPlugins(flutter::PluginRegistry* registry) {
  DesktopWebviewAuthPluginRegisterWithRegistrar(
      registry->GetRegistrarForPlugin("DesktopWebviewAuthPlugin"));
=======
#include <firebase_core/firebase_core_plugin_c_api.h>

void RegisterPlugins(flutter::PluginRegistry* registry) {
>>>>>>> Stashed changes
  FirebaseCorePluginCApiRegisterWithRegistrar(
      registry->GetRegistrarForPlugin("FirebaseCorePluginCApi"));
}
