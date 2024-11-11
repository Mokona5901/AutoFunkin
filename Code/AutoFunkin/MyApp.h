/***************************************************************
 * Name:      MyApp.h
 * Purpose:   Defines Application Class
 * Author:    Éric Laly (elaly@free.fr)
 * Created:   2007-09-21
 * Copyright: Éric Laly ()
 * License:
 **************************************************************/

#ifndef MYAPP_H
#define MYAPP_H

#include <wx/app.h>


class MyApp : public wxApp
{
    public:
        virtual bool OnInit();
    private:
        wxLocale m_locale;
};

#endif // MYAPP_H
