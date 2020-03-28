Action()
	
	
{   lr_start_transaction("add_members");

   	//新增会员
    web_reg_save_param_json(
		"ParamName=add_members checkpiont",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
   	web_submit_data("add_members",
		"Action=https://snailpet.com/v2/Members/add",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=error", "Value=0", ENDITEM,
		"Name=data", "Value=586435", ENDITEM,
		LAST);
   	if (atoi(lr_eval_string("{addID}"))==atoi(lr_eval_string("{add_membersByjson}"))){	
		lr_end_transaction("add_members", LR_PASS);		
	}else{
		lr_end_transaction("add_members", LR_FAIL);
	}
   	
   	
   	lr_start_transaction("add_product");
   	
   	//新增商品
   	web_reg_save_param_json(
		"ParamName=add_product checkpiont",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
   	web_submit_data("add_product",
		"Action=https://snailpet.com/v2/Product/add",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=shopId", "Value=17541", ENDITEM,
		"Name=productId", "Value=0", ENDITEM,
		"Name=barCode", "Value=111111", ENDITEM,
		"Name=isServer", "Value=0", ENDITEM,
		"Name=name", "Value=狗饼干", ENDITEM,
		"Name=inPrice", "Value=1", ENDITEM,
		"Name=outPrice", "Value=5", ENDITEM,
		LAST);
    if (atoi(lr_eval_string("{addID}"))==atoi(lr_eval_string("{add_productByjson}"))){	
		lr_end_transaction("add_product", LR_PASS);		
	}else{
		lr_end_transaction("add_product", LR_FAIL);
	}
   	
   	//收银
   	lr_start_transaction("cash_save");
   	
   	web_reg_save_param_json(
		"ParamName=cash_save checkpiont",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
   	web_submit_data("cash_save",
		"Action=https://snailpet.com/v2/cart/cash_save",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=shop_id", "Value=17541", ENDITEM,
		"Name=out_id", "Value=0", ENDITEM,
		"Name=cart_type", "Value=0", ENDITEM,
		LAST);
	if (atoi(lr_eval_string("{cash_saveID}"))==atoi(lr_eval_string("{cash_saveByjson}"))){	
		lr_end_transaction("cash_save", LR_PASS);		
	}else{
		lr_end_transaction("cash_save", LR_FAIL);
	}
   	
   	//查询销售
   	lr_start_transaction("action");
	web_reg_save_param_json(
		"ParamName=action",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
   	web_submit_data("action",
		"Action=https://snailpet.com/v2/analysis_es/action",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=ex_current_page", "Value= 首页", ENDITEM,
		"Name=ex_kind", "Value=点击", ENDITEM,
		"Name=ex_next_page", "Value=查询销售", ENDITEM,
		"Name=ex_title", "Value=查询销售", ENDITEM,
		"Name=shop_id", "Value=17541", ENDITEM,
		LAST);
   	if (atoi(lr_eval_string("{actionID}"))==atoi(lr_eval_string("{actionByjson}"))){	
		lr_end_transaction("action", LR_PASS);		
	}else{
		lr_end_transaction("action", LR_FAIL);
	}
	//消息提醒中的查看综合消息
	lr_start_transaction("user_read");
	web_reg_save_param_json(
		"ParamName=user_read",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	web_submit_data("user_read",
		"Action=https://snailpet.com/v2/message/user/read",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=message_id", "Value=1691797", ENDITEM,
		"Name=shop_id", "Value=17541", ENDITEM,
		LAST);
	if (atoi(lr_eval_string("{user_readID}"))==atoi(lr_eval_string("{user_readByjson}"))){	
		lr_end_transaction("user_read", LR_PASS);		
	}else{
		lr_end_transaction("user_read", LR_FAIL);
	}
	
	
	
	
	
	return 0;
}
