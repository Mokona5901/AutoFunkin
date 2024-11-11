/***************************************************************
 * Name:      MyApp.cpp
 * Purpose:   Code for Application Class
 * Author:    Éric Laly (elaly@free.fr)
 * Created:   2007-09-21
 * Copyright: Éric Laly ()
 * License:
 **************************************************************/

#ifdef WX_PRECOMP
#include "wx_pch.h"
#endif

#ifdef __BORLANDC__
#pragma hdrstop
#endif //__BORLANDC__

#include "MyApp.h"
#include "EvtFramePrincipal.h"

IMPLEMENT_APP(MyApp);

bool MyApp::OnInit()
{
    // on choisit le français comme langue
    m_locale.Init(wxLANGUAGE_FRENCH );

    EvtFramePrincipal* frame_principal = new EvtFramePrincipal(0);
    frame_principal->Show();

    return true;
}
