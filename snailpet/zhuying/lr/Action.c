Action()
{
	//定义一个检查点
	web_reg_find("SaveCount=homepage_checkpoint",
		"TextPfx=<title>",
		"TextSfx=</title>",
		LAST);
	
	//定义一个Get请求
	web_url("open homepage",
		"URL=https://snailpet.com/index",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);

	web_reg_find("SaveCount=login_checkpoint",
		"Text=error",
		LAST);
	
	//登录事务
	lr_start_transaction("login");
	
	//定义登录Post请求
	web_submit_data("login request",
		"Action=https://snailpet.com/v2/Passport/login",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=password", "Value={password}", ENDITEM,
		"Name=phone", "Value={phone}", ENDITEM,
		"Name=shop_id", "Value=null", ENDITEM,
		LAST);
	
	//登录断言
	if (atoi(lr_eval_string("{login_checkpoint}")) == 1){
		lr_output_message("login test success");
		lr_end_transaction("login", LR_PASS);
	} else {
		lr_output_message("login test fail");
		lr_end_transaction("login", LR_FAIL);
	}
	
	//新增商品检查点
	web_reg_save_param_json(
		"ParamName=add_goods checkpoint",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//新增商品事务
	lr_start_transaction("add_goods");
	
	//定义新增商品Post请求
	web_submit_data("add_goods_data",
		"Action=https://snailpet.com/v2/Product/add",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=shopId", "Value=17546", ENDITEM,
		"Name=productId", "Value=0", ENDITEM,
		"Name=isServer", "Value=1", ENDITEM,
		"Name=name", "Value=染发", ENDITEM,
		"Name=categoryId", "Value=841134", ENDITEM,
		"Name=inPrice", "Value=10", ENDITEM,
		"Name=outPrice", "Value=20", ENDITEM,
		"Name=percentage", "Value=0", ENDITEM,
		"Name=notice_stocks", "Value=1", ENDITEM,
		"Name=weight", "Value=0", ENDITEM,
		"Name=logo_images", "Value=", ENDITEM,
		"Name=detail_images", "Value=", ENDITEM,
		"Name=production_time", "Value=", ENDITEM,
		"Name=brand_name", "Value=", ENDITEM,
		"Name=version", "Value=1", ENDITEM,
		"Name=shop_id", "Value=17546", ENDITEM,
		LAST);

	//新增商品断言
	if (atoi(lr_eval_string("{addgoods_checkpoint}")) == 0){
		lr_output_message("addgoods test success");
		lr_end_transaction("add_goods", LR_PASS);
	} else {
		lr_output_message("addgoods test fail");
		lr_end_transaction("add_goods", LR_FAIL);
	}
	
	//商品入库检查点
	web_reg_save_param_json(
		"ParamName=goods_stock checkpoint",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//商品入库事务
	lr_start_transaction("goods_stock");
	
	//定义商品入库Post请求
	web_submit_data("goods_stock_data",
		"Action=https://snailpet.com/v2/product/update/stocks",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=exp_time", "Value=null", ENDITEM,
		"Name=inPrice", "Value=5", ENDITEM,
		"Name=mark", "Value=", ENDITEM,
		"Name=number", "Value=15", ENDITEM,
		"Name=productId", "Value=2133300", ENDITEM,
		"Name=production_time", "Value=null", ENDITEM,
		"Name=shelf_life", "Value=0", ENDITEM,
		"Name=shop_id", "Value=17546", ENDITEM,
		"Name=shopId", "Value=17546", ENDITEM,
		LAST);

	//商品入库断言
	if (atoi(lr_eval_string("{goods_stock checkpoint}")) == 0){
		lr_output_message("goodstock test success");
		lr_end_transaction("goods_stock", LR_PASS);
	} else {
		lr_output_message("goodstock test fail");
		lr_end_transaction("goods_stock", LR_FAIL);
	}
	
	
	//新增会员检查点
	web_reg_save_param_json(
		"ParamName=add_customer checkpoint",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//新增会员事务
	lr_start_transaction("add_customer");
	
	//定义新增会员Post请求
	web_submit_data("add_customer_data",
		"Action=https://snailpet.com/v2/Members/add",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=addr", "Value=", ENDITEM,
		"Name=cardNumber", "Value=", ENDITEM,
		"Name=is_open_upgrade", "Value=1", ENDITEM,
		"Name=is_spending_msg", "Value=1", ENDITEM,
		"Name=mark", "Value=", ENDITEM,
		"Name=member_tags", "Value=", ENDITEM,
		"Name=name", "Value={addname}", ENDITEM,
		"Name=pets", "Value=[]", ENDITEM,
		"Name=phone", "Value={addphone}", ENDITEM,
		"Name=sex", "Value=", ENDITEM,
		"Name=shop_id", "Value=17546", ENDITEM,
		"Name=shopId", "Value=17546", ENDITEM,
		"Name=spare_phone", "Value=", ENDITEM,
		LAST);

	//新增会员断言
	if (atoi(lr_eval_string("{add_customer checkpoint}")) == 0){
		lr_output_message("addcustomer test success");
		lr_end_transaction("add_customer", LR_PASS);
	} else {
		lr_output_message("addcustomer test fail");
		lr_end_transaction("add_customer", LR_FAIL);
	}
	
	//余额充值检查点
	web_reg_save_param_json(
		"ParamName=recharge checkpoint",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//余额充值事务
	lr_start_transaction("customer recharge");
	
	//定义余额充值Post请求
	web_submit_data("recharge_data",
		"Action=https://snailpet.com/v2/members/level/recharge",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=amount", "Value=100", ENDITEM,
		"Name=cardId", "Value=0", ENDITEM,
		"Name=member_id", "Value=586109", ENDITEM,
		"Name=number", "Value=100", ENDITEM,
		"Name=pay_way", "Value=3", ENDITEM,
		"Name=percentage", "Value=0", ENDITEM,
		"Name=sale_user_id", "Value=27363", ENDITEM,
		"Name=shop_id", "Value=17546", ENDITEM,
		"Name=shop_level_id", "Value=0", ENDITEM,
		"Name=trade_no", "Value=", ENDITEM,
		"Name=version", "Value=1", ENDITEM,
		LAST);

	//余额充值断言
	if (atoi(lr_eval_string("{recharge checkpoint}")) == 0){
		lr_output_message("recharge test success");
		lr_end_transaction("customer recharge", LR_PASS);
	} else {
		lr_output_message("recharge test fail");
		lr_end_transaction("customer recharge", LR_FAIL);
	}
	
	return 0;
}
