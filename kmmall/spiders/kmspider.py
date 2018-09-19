# -*- coding: utf-8 -*-
import scrapy

from kmmall.items import KmmallItem


class KmspiderSpider(scrapy.Spider):
    name = 'kmspider'
    allowed_domains = ['km1818.com']
#     start_urls = ["http://search.km1818.com/10/c-list-13700.html","http://search.km1818.com/10/c-list-14529.html"
# ,"http://search.km1818.com/10/c-list-14531.html"
# ,"http://search.km1818.com/10/c-list-14539.html"
# ,"http://search.km1818.com/10/c-list-2986.html"
# ,"http://search.km1818.com/10/c-list-14538.html"
# ,"http://search.km1818.com/10/c-list-14536.html"
# ,"http://search.km1818.com/10/c-list-14535.html"
# ,"http://search.km1818.com/10/c-list-14534.html"
# ,"http://search.km1818.com/10/c-list-14533.html"
# ,"http://search.km1818.com/10/c-list-14541.html"
# ,"http://search.km1818.com/10/c-list-3001.html"
# ,"http://search.km1818.com/10/c-list-3003.html"
# ,"http://search.km1818.com/10/c-list-2996.html"
# ,"http://search.km1818.com/10/c-list-2997.html"
# ,"http://search.km1818.com/10/c-list-2999.html"
# ,"http://search.km1818.com/10/c-list-14626.html"
# ,"http://search.km1818.com/10/c-list-14625.html"
# ,"http://search.km1818.com/10/c-list-3002.html"
# ,"http://search.km1818.com/10/c-list-3000.html"
# ,"http://search.km1818.com/10/c-list-2998.html"
# ,"http://search.km1818.com/10/c-list-14663.html"
# ,"http://search.km1818.com/10/c-list-14665.html"
# ,"http://search.km1818.com/10/c-list-14664.html"
# ,"http://search.km1818.com/10/c-list-14661.html"
# ,"http://search.km1818.com/10/c-list-14672.html"
# ,"http://search.km1818.com/10/c-list-14670.html"
# ,"http://search.km1818.com/10/c-list-14669.html"
# ,"http://search.km1818.com/10/c-list-14667.html"
# ,"http://search.km1818.com/10/c-list-14666.html"
# ,"http://search.km1818.com/10/c-list-14668.html"
# ,"http://search.km1818.com/10/c-list-14706.html"
# ,"http://search.km1818.com/10/c-list-14705.html"
# ,"http://search.km1818.com/10/c-list-14704.html"
# ,"http://search.km1818.com/10/c-list-14703.html"
# ,"http://search.km1818.com/10/c-list-14707.html"
# ,"http://search.km1818.com/10/c-list-14700.html"
# ,"http://search.km1818.com/10/c-list-14699.html"
# ,"http://search.km1818.com/10/c-list-14698.html"
# ,"http://search.km1818.com/10/c-list-14697.html"
# ,"http://search.km1818.com/10/c-list-14701.html"
# ,"http://search.km1818.com/10/c-list-14645.html"
# ,"http://search.km1818.com/10/c-list-14646.html"
# ,"http://search.km1818.com/10/c-list-14640.html"
# ,"http://search.km1818.com/10/c-list-14642.html"
# ,"http://search.km1818.com/10/c-list-14644.html"
# ,"http://search.km1818.com/10/c-list-14643.html"
# ,"http://search.km1818.com/10/c-list-13653.html"
# ,"http://search.km1818.com/10/c-list-13651.html"
# ,"http://search.km1818.com/10/c-list-13654.html"
# ,"http://search.km1818.com/10/c-list-13649.html"
# ,"http://search.km1818.com/10/c-list-13650.html"
# ,"http://search.km1818.com/10/c-list-13638.html"
# ,"http://search.km1818.com/10/c-list-13637.html"
# ,"http://search.km1818.com/10/c-list-13639.html"
# ,"http://search.km1818.com/10/c-list-13640.html"
# ,"http://search.km1818.com/10/c-list-13618.html"
# ,"http://search.km1818.com/10/c-list-13622.html"
# ,"http://search.km1818.com/10/c-list-13623.html"
# ,"http://search.km1818.com/10/c-list-13627.html"
# ,"http://search.km1818.com/10/c-list-13619.html"
# ,"http://search.km1818.com/10/c-list-13620.html"
# ,"http://search.km1818.com/10/c-list-13621.html"
# ,"http://search.km1818.com/10/c-list-13624.html"
# ,"http://search.km1818.com/10/c-list-13625.html"
# ,"http://search.km1818.com/10/c-list-13628.html"
# ,"http://search.km1818.com/10/c-list-14655.html"
# ,"http://search.km1818.com/10/c-list-14654.html"
# ,"http://search.km1818.com/10/c-list-14653.html"
# ,"http://search.km1818.com/10/c-list-14652.html"
# ,"http://search.km1818.com/10/c-list-14651.html"
# ,"http://search.km1818.com/10/c-list-14649.html"
# ,"http://search.km1818.com/10/c-list-14650.html"
# ,"http://search.km1818.com/10/c-list-2651.html"
# ,"http://search.km1818.com/10/c-list-2641.html"
# ,"http://search.km1818.com/10/c-list-3422.html"
# ,"http://search.km1818.com/10/c-list-2643.html"
# ,"http://search.km1818.com/10/c-list-14159.html"
# ,"http://search.km1818.com/10/c-list-6862.html"
# ,"http://search.km1818.com/10/c-list-2652.html"
# ,"http://search.km1818.com/10/c-list-2650.html"
# ,"http://search.km1818.com/10/c-list-2640.html"
# ,"http://search.km1818.com/10/c-list-2642.html"
# ,"http://search.km1818.com/10/c-list-2654.html"
# ,"http://search.km1818.com/10/c-list-2659.html"
# ,"http://search.km1818.com/10/c-list-2655.html"
# ,"http://search.km1818.com/10/c-list-2653.html"
# ,"http://search.km1818.com/10/c-list-2656.html"
# ,"http://search.km1818.com/10/c-list-5963.html"
# ,"http://search.km1818.com/10/c-list-3450.html"
# ,"http://search.km1818.com/10/c-list-4382.html"
# ,"http://search.km1818.com/10/c-list-2664.html"
# ,"http://search.km1818.com/10/c-list-2722.html"
# ,"http://search.km1818.com/10/c-list-14481.html"
# ,"http://search.km1818.com/10/c-list-2662.html"
# ,"http://search.km1818.com/10/c-list-14219.html"
# ,"http://search.km1818.com/10/c-list-14162.html"
# ,"http://search.km1818.com/10/c-list-14163.html"
# ,"http://search.km1818.com/10/c-list-14165.html"
# ,"http://search.km1818.com/10/c-list-14213.html"
# ,"http://search.km1818.com/10/c-list-4383.html"
# ,"http://search.km1818.com/10/c-list-14202.html"
# ,"http://search.km1818.com/10/c-list-14203.html"
# ,"http://search.km1818.com/10/c-list-14212.html"
# ,"http://search.km1818.com/10/c-list-14214.html"
# ,"http://search.km1818.com/10/c-list-14215.html"
# ,"http://search.km1818.com/10/c-list-14218.html"
# ,"http://search.km1818.com/10/c-list-14217.html"
# ,"http://search.km1818.com/10/c-list-14216.html"
# ,"http://search.km1818.com/10/c-list-14211.html"
# ,"http://search.km1818.com/10/c-list-14210.html"
# ,"http://search.km1818.com/10/c-list-5882.html"
# ,"http://search.km1818.com/10/c-list-5964.html"
# ,"http://search.km1818.com/10/c-list-5965.html"
# ,"http://search.km1818.com/10/c-list-5864.html"
# ,"http://search.km1818.com/10/c-list-14498.html"
# ,"http://search.km1818.com/10/c-list-14205.html"
# ,"http://search.km1818.com/10/c-list-14206.html"
# ,"http://search.km1818.com/10/c-list-14207.html"
# ,"http://search.km1818.com/10/c-list-14208.html"
# ,"http://search.km1818.com/10/c-list-14209.html"
# ,"http://search.km1818.com/10/c-list-5384.html"
# ,"http://search.km1818.com/10/c-list-5962.html"
# ,"http://search.km1818.com/10/c-list-2733.html"
# ,"http://search.km1818.com/10/c-list-2735.html"
# ,"http://search.km1818.com/10/c-list-2742.html"
# ,"http://search.km1818.com/10/c-list-2737.html"
# ,"http://search.km1818.com/10/c-list-2739.html"
# ,"http://search.km1818.com/10/c-list-3442.html"
# ,"http://search.km1818.com/10/c-list-2744.html"
# ,"http://search.km1818.com/10/c-list-14200.html"
# ,"http://search.km1818.com/10/c-list-14231.html"
# ,"http://search.km1818.com/10/c-list-14233.html"
# ,"http://search.km1818.com/10/c-list-14230.html"
# ,"http://search.km1818.com/10/c-list-14229.html"
# ,"http://search.km1818.com/10/c-list-14228.html"
# ,"http://search.km1818.com/10/c-list-14232.html"
# ,"http://search.km1818.com/10/c-list-5242.html"
# ,"http://search.km1818.com/10/c-list-4994.html"
# ,"http://search.km1818.com/10/c-list-4990.html"
# ,"http://search.km1818.com/10/c-list-4995.html"
# ,"http://search.km1818.com/10/c-list-4992.html"
# ,"http://search.km1818.com/10/c-list-4985.html"
# ,"http://search.km1818.com/10/c-list-6703.html"
# ,"http://search.km1818.com/10/c-list-4056.html"
# ,"http://search.km1818.com/10/c-list-4993.html"
# ,"http://search.km1818.com/10/c-list-6702.html"
# ,"http://search.km1818.com/10/c-list-4996.html"
# ,"http://search.km1818.com/10/c-list-4991.html"
# ,"http://search.km1818.com/10/c-list-4986.html"
# ,"http://search.km1818.com/10/c-list-4987.html"
# ,"http://search.km1818.com/10/c-list-14554.html"
# ,"http://search.km1818.com/10/c-list-14550.html"
# ,"http://search.km1818.com/10/c-list-14556.html"
# ,"http://search.km1818.com/10/c-list-14558.html"
# ,"http://search.km1818.com/10/c-list-8067.html"
# ,"http://search.km1818.com/10/c-list-14658.html"
# ,"http://search.km1818.com/10/c-list-8425.html"
# ,"http://search.km1818.com/10/c-list-14662.html"
# ,"http://search.km1818.com/10/c-list-14660.html"
# ,"http://search.km1818.com/10/c-list-14659.html"
# ,"http://search.km1818.com/10/c-list-13265.html"
# ,"http://search.km1818.com/10/c-list-14656.html"
# ,"http://search.km1818.com/10/c-list-8136.html"
# ,"http://search.km1818.com/10/c-list-8137.html"
# ,"http://search.km1818.com/10/c-list-8131.html"
# ,"http://search.km1818.com/10/c-list-8133.html"
# ,"http://search.km1818.com/10/c-list-8135.html"
# ,"http://search.km1818.com/10/c-list-8132.html"
# ,"http://search.km1818.com/10/c-list-8134.html"
# ,"http://search.km1818.com/10/c-list-9086.html"
# ,"http://search.km1818.com/10/c-list-9083.html"
# ,"http://search.km1818.com/10/c-list-9092.html"
# ,"http://search.km1818.com/10/c-list-9095.html"
# ,"http://search.km1818.com/10/c-list-14679.html"
# ,"http://search.km1818.com/10/c-list-14675.html"
# ,"http://search.km1818.com/10/c-list-14676.html"
# ,"http://search.km1818.com/10/c-list-9087.html"
# ,"http://search.km1818.com/10/c-list-14677.html"
# ,"http://search.km1818.com/10/c-list-9082.html"
# ,"http://search.km1818.com/10/c-list-9102.html"
# ,"http://search.km1818.com/10/c-list-14674.html"
# ,"http://search.km1818.com/10/c-list-9098.html"
# ,"http://search.km1818.com/10/c-list-14678.html"
# ,"http://search.km1818.com/10/c-list-9097.html"
# ,"http://search.km1818.com/10/c-list-9090.html"
# ,"http://search.km1818.com/10/c-list-13589.html"
# ,"http://search.km1818.com/10/c-list-13588.html"
# ,"http://search.km1818.com/10/c-list-14688.html"
# ,"http://search.km1818.com/10/c-list-14687.html"
# ,"http://search.km1818.com/10/c-list-14685.html"
# ,"http://search.km1818.com/10/c-list-14695.html"
# ,"http://search.km1818.com/10/c-list-14684.html"
# ,"http://search.km1818.com/10/c-list-14694.html"
# ,"http://search.km1818.com/10/c-list-14693.html"
# ,"http://search.km1818.com/10/c-list-14692.html"
# ,"http://search.km1818.com/10/c-list-14690.html"
# ,"http://search.km1818.com/10/c-list-14689.html"
# ,"http://search.km1818.com/10/c-list-14682.html"
# ,"http://search.km1818.com/10/c-list-14681.html"
# ,"http://search.km1818.com/10/c-list-14680.html"
# ,"http://search.km1818.com/10/c-list-14477.html"
# ,"http://search.km1818.com/10/c-list-7964.html"
# ,"http://search.km1818.com/10/c-list-8026.html"
# ,"http://search.km1818.com/10/c-list-8022.html"
# ,"http://search.km1818.com/10/c-list-8023.html"
# ,"http://search.km1818.com/10/c-list-7965.html"
# ,"http://search.km1818.com/10/c-list-14482.html"
# ,"http://search.km1818.com/10/c-list-14483.html"
# ,"http://search.km1818.com/10/c-list-14479.html"
# ,"http://search.km1818.com/10/c-list-14462.html"
# ,"http://search.km1818.com/10/c-list-8027.html"
# ,"http://search.km1818.com/10/c-list-8405.html"
# ,"http://search.km1818.com/10/c-list-14599.html"
# ,"http://search.km1818.com/10/c-list-14587.html"
# ,"http://search.km1818.com/10/c-list-14594.html"
# ,"http://search.km1818.com/10/c-list-14595.html"
# ,"http://search.km1818.com/10/c-list-14580.html"
# ,"http://search.km1818.com/10/c-list-14578.html"
# ,"http://search.km1818.com/10/c-list-14576.html"
# ,"http://search.km1818.com/10/c-list-14574.html"
# ,"http://search.km1818.com/10/c-list-14568.html"
# ,"http://search.km1818.com/10/c-list-14586.html"
# ,"http://search.km1818.com/10/c-list-14582.html"
# ,"http://search.km1818.com/10/c-list-14596.html"
# ,"http://search.km1818.com/10/c-list-14593.html"
# ,"http://search.km1818.com/10/c-list-14592.html"
# ,"http://search.km1818.com/10/c-list-14591.html"
# ,"http://search.km1818.com/10/c-list-14589.html"
# ,"http://search.km1818.com/10/c-list-14588.html"
# ,"http://search.km1818.com/10/c-list-14600.html"
# ,"http://search.km1818.com/10/c-list-8062.html"
# ,"http://search.km1818.com/10/c-list-8057.html"
# ,"http://search.km1818.com/10/c-list-8056.html"
# ,"http://search.km1818.com/10/c-list-8055.html"
# ,"http://search.km1818.com/10/c-list-8058.html"
# ,"http://search.km1818.com/10/c-list-8059.html"
# ,"http://search.km1818.com/10/c-list-8061.html"
# ,"http://search.km1818.com/10/c-list-14712.html"
# ,"http://search.km1818.com/10/c-list-14709.html"
# ,"http://search.km1818.com/10/c-list-14710.html"
# ,"http://search.km1818.com/10/c-list-14711.html"
# ,"http://search.km1818.com/10/c-list-14713.html"
# ,"http://search.km1818.com/10/c-list-14715.html"
# ,"http://search.km1818.com/10/c-list-14716.html"
# ,"http://search.km1818.com/10/c-list-14505.html"
# ,"http://search.km1818.com/10/c-list-14575.html"
# ,"http://search.km1818.com/10/c-list-14597.html"
# ,"http://search.km1818.com/10/c-list-14598.html"
# ,"http://search.km1818.com/10/c-list-14602.html"
# ,"http://search.km1818.com/10/c-list-14605.html"
# ,"http://search.km1818.com/10/c-list-14579.html"
# ,"http://search.km1818.com/10/c-list-14583.html"
# ,"http://search.km1818.com/10/c-list-14601.html"
# ,"http://search.km1818.com/10/c-list-14604.html"
# ,"http://search.km1818.com/10/c-list-14560.html"
# ,"http://search.km1818.com/10/c-list-14563.html"
# ,"http://search.km1818.com/10/c-list-14564.html"
# ,"http://search.km1818.com/10/c-list-14567.html"
# ,"http://search.km1818.com/10/c-list-14570.html"
# ,"http://search.km1818.com/10/c-list-14571.html"
# ,"http://search.km1818.com/10/c-list-14559.html"
# ,"http://search.km1818.com/10/c-list-14565.html"
# ,"http://search.km1818.com/10/c-list-14561.html"
# ,"http://search.km1818.com/10/c-list-14500.html"
# ,"http://search.km1818.com/10/c-list-14502.html"
# ,"http://search.km1818.com/10/c-list-14504.html"
# ,"http://search.km1818.com/10/c-list-14572.html"
# ,"http://search.km1818.com/10/c-list-14501.html"
# ,"http://search.km1818.com/10/c-list-14519.html"
# ,"http://search.km1818.com/10/c-list-14513.html"
# ,"http://search.km1818.com/10/c-list-14517.html"
# ,"http://search.km1818.com/10/c-list-14515.html"
# ,"http://search.km1818.com/10/c-list-14512.html"
# ,"http://search.km1818.com/10/c-list-14510.html"
# ,"http://search.km1818.com/10/c-list-14520.html"
# ,"http://search.km1818.com/10/c-list-14632.html"
# ,"http://search.km1818.com/10/c-list-14525.html"
# ,"http://search.km1818.com/10/c-list-14532.html"
# ,"http://search.km1818.com/10/c-list-14522.html"
# ,"http://search.km1818.com/10/c-list-14521.html"
# ,"http://search.km1818.com/10/c-list-14509.html"
# ,"http://search.km1818.com/10/c-list-14530.html"
# ,"http://search.km1818.com/10/c-list-14528.html"
# ,"http://search.km1818.com/10/c-list-14523.html"
# ,"http://search.km1818.com/10/c-list-14527.html"
# ,"http://search.km1818.com/10/c-list-14552.html"
# ,"http://search.km1818.com/10/c-list-14553.html"
# ,"http://search.km1818.com/10/c-list-14547.html"
# ,"http://search.km1818.com/10/c-list-14555.html"
# ,"http://search.km1818.com/10/c-list-14544.html"
# ,"http://search.km1818.com/10/c-list-14537.html"
# ,"http://search.km1818.com/10/c-list-14542.html"
# ,"http://search.km1818.com/10/c-list-14545.html"
# ,"http://search.km1818.com/10/c-list-14548.html"
# ,"http://search.km1818.com/10/c-list-14508.html"
# ,"http://search.km1818.com/10/c-list-14557.html"
# ,"http://search.km1818.com/10/c-list-14630.html"
# ,"http://search.km1818.com/10/c-list-14609.html"
# ,"http://search.km1818.com/10/c-list-14507.html"
# ,"http://search.km1818.com/10/c-list-14631.html"
# ,"http://search.km1818.com/10/c-list-14623.html"
# ,"http://search.km1818.com/10/c-list-14614.html"
# ,"http://search.km1818.com/10/c-list-14610.html"
# ,"http://search.km1818.com/10/c-list-14612.html"
# ,"http://search.km1818.com/10/c-list-14613.html"
# ,"http://search.km1818.com/10/c-list-14615.html"
# ,"http://search.km1818.com/10/c-list-14616.html"
# ,"http://search.km1818.com/10/c-list-14611.html"
# ,"http://search.km1818.com/10/c-list-14629.html"
# ,"http://search.km1818.com/10/c-list-14628.html"
# ,"http://search.km1818.com/10/c-list-14620.html"
# ,"http://search.km1818.com/10/c-list-2802.html"
# ,"http://search.km1818.com/10/c-list-2803.html"
# ,"http://search.km1818.com/10/c-list-2804.html"
# ,"http://search.km1818.com/10/c-list-4322.html"
# ,"http://search.km1818.com/10/c-list-14070.html"
# ,"http://search.km1818.com/10/c-list-14072.html"
# ,"http://search.km1818.com/10/c-list-14073.html"
# ,"http://search.km1818.com/10/c-list-14074.html"
# ,"http://search.km1818.com/10/c-list-14076.html"
# ,"http://search.km1818.com/10/c-list-14127.html"
# ,"http://search.km1818.com/10/c-list-2798.html"
# ,"http://search.km1818.com/10/c-list-2797.html"
# ,"http://search.km1818.com/10/c-list-2796.html"
# ,"http://search.km1818.com/10/c-list-11085.html"
# ,"http://search.km1818.com/10/c-list-14071.html"
# ,"http://search.km1818.com/10/c-list-4242.html"
# ,"http://search.km1818.com/10/c-list-4950.html"
# ,"http://search.km1818.com/10/c-list-2800.html"
# ,"http://search.km1818.com/10/c-list-14119.html"
# ,"http://search.km1818.com/10/c-list-14106.html"
# ,"http://search.km1818.com/10/c-list-14080.html"
# ,"http://search.km1818.com/10/c-list-14081.html"
# ,"http://search.km1818.com/10/c-list-14125.html"
# ,"http://search.km1818.com/10/c-list-14124.html"
# ,"http://search.km1818.com/10/c-list-14123.html"
# ,"http://search.km1818.com/10/c-list-14122.html"
# ,"http://search.km1818.com/10/c-list-14121.html"
# ,"http://search.km1818.com/10/c-list-14118.html"
# ,"http://search.km1818.com/10/c-list-14096.html"
# ,"http://search.km1818.com/10/c-list-14126.html"
# ,"http://search.km1818.com/10/c-list-14078.html"
# ,"http://search.km1818.com/10/c-list-14079.html"
# ,"http://search.km1818.com/10/c-list-14036.html"
# ,"http://search.km1818.com/10/c-list-13656.html"
# ,"http://search.km1818.com/10/c-list-13658.html"
# ,"http://search.km1818.com/10/c-list-13657.html"
# ,"http://search.km1818.com/10/c-list-13668.html"
# ,"http://search.km1818.com/10/c-list-13666.html"
# ,"http://search.km1818.com/10/c-list-13665.html"
# ,"http://search.km1818.com/10/c-list-13664.html"
# ,"http://search.km1818.com/10/c-list-13663.html"
# ,"http://search.km1818.com/10/c-list-13662.html"
# ,"http://search.km1818.com/10/c-list-13661.html"
# ,"http://search.km1818.com/10/c-list-13660.html"
# ,"http://search.km1818.com/10/c-list-13659.html"
# ,"http://search.km1818.com/10/c-list-13673.html"
# ,"http://search.km1818.com/10/c-list-13678.html"
# ,"http://search.km1818.com/10/c-list-13679.html"
# ,"http://search.km1818.com/10/c-list-13672.html"
# ,"http://search.km1818.com/10/c-list-13675.html"
# ,"http://search.km1818.com/10/c-list-13676.html"
# ,"http://search.km1818.com/10/c-list-13674.html"
# ,"http://search.km1818.com/10/c-list-13680.html"
# ,"http://search.km1818.com/10/c-list-13681.html"
# ,"http://search.km1818.com/10/c-list-13682.html"
# ,"http://search.km1818.com/10/c-list-13683.html"
# ,"http://search.km1818.com/10/c-list-13684.html"
# ,"http://search.km1818.com/10/c-list-13685.html"
# ,"http://search.km1818.com/10/c-list-13677.html"
# ,"http://search.km1818.com/10/c-list-14475.html"
# ,"http://search.km1818.com/10/c-list-14526.html"
# ,"http://search.km1818.com/10/c-list-14393.html"
# ,"http://search.km1818.com/10/c-list-14396.html"
# ,"http://search.km1818.com/10/c-list-14397.html"
# ,"http://search.km1818.com/10/c-list-14398.html"
# ,"http://search.km1818.com/10/c-list-14399.html"
# ,"http://search.km1818.com/10/c-list-14400.html"
# ,"http://search.km1818.com/10/c-list-14401.html"
# ,"http://search.km1818.com/10/c-list-14402.html"
# ,"http://search.km1818.com/10/c-list-14403.html"
# ,"http://search.km1818.com/10/c-list-14404.html"
# ,"http://search.km1818.com/10/c-list-14405.html"
# ,"http://search.km1818.com/10/c-list-14407.html"
# ,"http://search.km1818.com/10/c-list-14408.html"
# ,"http://search.km1818.com/10/c-list-14409.html"
# ,"http://search.km1818.com/10/c-list-14410.html"
# ,"http://search.km1818.com/10/c-list-14411.html"
# ,"http://search.km1818.com/10/c-list-14415.html"
# ,"http://search.km1818.com/10/c-list-14416.html"
# ,"http://search.km1818.com/10/c-list-14412.html"
# ,"http://search.km1818.com/10/c-list-14413.html"
# ,"http://search.km1818.com/10/c-list-14414.html"
# ,"http://search.km1818.com/10/c-list-14392.html"
# ,"http://search.km1818.com/10/c-list-14394.html"
# ,"http://search.km1818.com/10/c-list-14395.html"
# ,"http://search.km1818.com/10/c-list-14406.html"
# ,"http://search.km1818.com/10/c-list-14417.html"
# ,"http://search.km1818.com/10/c-list-14418.html"
# ,"http://search.km1818.com/10/c-list-14446.html"
# ,"http://search.km1818.com/10/c-list-14454.html"
# ,"http://search.km1818.com/10/c-list-14459.html"
# ,"http://search.km1818.com/10/c-list-14460.html"
# ,"http://search.km1818.com/10/c-list-14461.html"
# ,"http://search.km1818.com/10/c-list-14468.html"
# ,"http://search.km1818.com/10/c-list-14489.html"
# ,"http://search.km1818.com/10/c-list-14497.html"
# ,"http://search.km1818.com/10/c-list-14499.html"
# ,"http://search.km1818.com/10/c-list-14503.html"
# ,"http://search.km1818.com/10/c-list-14506.html"
# ,"http://search.km1818.com/10/c-list-14511.html"
# ,"http://search.km1818.com/10/c-list-14514.html"
# ,"http://search.km1818.com/10/c-list-14516.html"
# ,"http://search.km1818.com/10/c-list-14518.html"
# ,"http://search.km1818.com/10/c-list-14524.html"
# ,"http://search.km1818.com/10/c-list-14540.html"
# ,"http://search.km1818.com/10/c-list-14543.html"
# ,"http://search.km1818.com/10/c-list-14546.html"
# ,"http://search.km1818.com/10/c-list-14551.html"
# ,"http://search.km1818.com/10/c-list-14562.html"
# ,"http://search.km1818.com/10/c-list-14569.html"
# ,"http://search.km1818.com/10/c-list-14573.html"
# ,"http://search.km1818.com/10/c-list-14577.html"
# ,"http://search.km1818.com/10/c-list-14581.html"
# ,"http://search.km1818.com/10/c-list-14584.html"
# ,"http://search.km1818.com/10/c-list-14585.html"
# ,"http://search.km1818.com/10/c-list-14590.html"
# ,"http://search.km1818.com/10/c-list-14603.html"
# ,"http://search.km1818.com/10/c-list-14606.html"
# ,"http://search.km1818.com/10/c-list-14608.html"
# ,"http://search.km1818.com/10/c-list-14617.html"
# ,"http://search.km1818.com/10/c-list-14619.html"
# ,"http://search.km1818.com/10/c-list-14621.html"
# ,"http://search.km1818.com/10/c-list-14622.html"
# ,"http://search.km1818.com/10/c-list-14637.html"
# ,"http://search.km1818.com/10/c-list-14627.html"
# ,"http://search.km1818.com/10/c-list-14633.html"
# ,"http://search.km1818.com/10/c-list-14634.html"
# ,"http://search.km1818.com/10/c-list-14635.html"
# ,"http://search.km1818.com/10/c-list-14624.html"
# ,"http://search.km1818.com/10/c-list-14458.html"
# ,"http://search.km1818.com/10/c-list-14456.html"
# ,"http://search.km1818.com/10/c-list-14455.html"
# ,"http://search.km1818.com/10/c-list-14453.html"
# ,"http://search.km1818.com/10/c-list-14450.html"
# ,"http://search.km1818.com/10/c-list-14449.html"
# ,"http://search.km1818.com/10/c-list-14452.html"
# ,"http://search.km1818.com/10/c-list-14457.html"
# ,"http://search.km1818.com/10/c-list-14451.html"
# ,"http://search.km1818.com/10/c-list-14448.html"
# ,"http://search.km1818.com/10/c-list-3060.html"
# ,"http://search.km1818.com/10/c-list-10665.html"
# ,"http://search.km1818.com/10/c-list-10625.html"
# ,"http://search.km1818.com/10/c-list-3066.html"
# ,"http://search.km1818.com/10/c-list-3061.html"
# ,"http://search.km1818.com/10/c-list-14419.html"
# ,"http://search.km1818.com/10/c-list-10751.html"
# ,"http://search.km1818.com/10/c-list-4782.html"
# ,"http://search.km1818.com/10/c-list-12326.html"
# ,"http://search.km1818.com/10/c-list-12322.html"
# ,"http://search.km1818.com/10/c-list-14424.html"
# ,"http://search.km1818.com/10/c-list-14428.html"
# ,"http://search.km1818.com/10/c-list-14427.html"
# ,"http://search.km1818.com/10/c-list-14425.html"
# ,"http://search.km1818.com/10/c-list-14423.html"
# ,"http://search.km1818.com/10/c-list-14422.html"
# ,"http://search.km1818.com/10/c-list-14421.html"
# ,"http://search.km1818.com/10/c-list-14420.html"
# ,"http://search.km1818.com/10/c-list-14466.html"
# ,"http://search.km1818.com/10/c-list-5543.html"
# ,"http://search.km1818.com/10/c-list-8523.html"
# ,"http://search.km1818.com/10/c-list-8502.html"
# ,"http://search.km1818.com/10/c-list-4804.html"
# ,"http://search.km1818.com/10/c-list-4802.html"
# ,"http://search.km1818.com/10/c-list-14469.html"
# ,"http://search.km1818.com/10/c-list-14463.html"
# ,"http://search.km1818.com/10/c-list-14464.html"
# ,"http://search.km1818.com/10/c-list-10866.html"
# ,"http://search.km1818.com/10/c-list-5544.html"
# ,"http://search.km1818.com/10/c-list-14467.html"
# ,"http://search.km1818.com/10/c-list-14471.html"
# ,"http://search.km1818.com/10/c-list-14473.html"
# ,"http://search.km1818.com/10/c-list-14472.html"
# ,"http://search.km1818.com/10/c-list-14474.html"
# ,"http://search.km1818.com/10/c-list-14476.html"
# ,"http://search.km1818.com/10/c-list-12327.html"
# ,"http://search.km1818.com/10/c-list-14484.html"
# ,"http://search.km1818.com/10/c-list-14486.html"
# ,"http://search.km1818.com/10/c-list-14487.html"
# ,"http://search.km1818.com/10/c-list-14490.html"
# ,"http://search.km1818.com/10/c-list-14480.html"
# ,"http://search.km1818.com/10/c-list-12309.html"
# ,"http://search.km1818.com/10/c-list-12303.html"
# ,"http://search.km1818.com/10/c-list-14433.html"
# ,"http://search.km1818.com/10/c-list-14435.html"
# ,"http://search.km1818.com/10/c-list-14432.html"
# ,"http://search.km1818.com/10/c-list-14431.html"
# ,"http://search.km1818.com/10/c-list-14430.html"
# ,"http://search.km1818.com/10/c-list-14429.html"
# ,"http://search.km1818.com/10/c-list-13439.html"
# ,"http://search.km1818.com/10/c-list-14434.html"
# ,"http://search.km1818.com/10/c-list-14445.html"
# ,"http://search.km1818.com/10/c-list-14439.html"
# ,"http://search.km1818.com/10/c-list-14438.html"
# ,"http://search.km1818.com/10/c-list-14440.html"
# ,"http://search.km1818.com/10/c-list-14444.html"
# ,"http://search.km1818.com/10/c-list-14441.html"
# ,"http://search.km1818.com/10/c-list-14442.html"
# ,"http://search.km1818.com/10/c-list-14443.html"
# ,"http://search.km1818.com/10/c-list-8144.html"
# ,"http://search.km1818.com/10/c-list-8145.html"
# ,"http://search.km1818.com/10/c-list-14745.html"
# ,"http://search.km1818.com/10/c-list-14744.html"
# ,"http://search.km1818.com/10/c-list-14749.html"
# ,"http://search.km1818.com/10/c-list-14750.html"
# ,"http://search.km1818.com/10/c-list-14770.html"
# ,"http://search.km1818.com/10/c-list-14776.html"
# ,"http://search.km1818.com/10/c-list-14777.html"
# ,"http://search.km1818.com/10/c-list-14778.html"
# ,"http://search.km1818.com/10/c-list-14742.html"
# ,"http://search.km1818.com/10/c-list-14743.html"
# ,"http://search.km1818.com/10/c-list-14739.html"
# ,"http://search.km1818.com/10/c-list-14753.html"
# ,"http://search.km1818.com/10/c-list-14736.html"
# ,"http://search.km1818.com/10/c-list-8148.html"
# ,"http://search.km1818.com/10/c-list-8147.html"
# ,"http://search.km1818.com/10/c-list-8146.html"
# ,"http://search.km1818.com/10/c-list-14738.html"
# ,"http://search.km1818.com/10/c-list-14740.html"
# ,"http://search.km1818.com/10/c-list-14741.html"
# ,"http://search.km1818.com/10/c-list-14737.html"
# ,"http://search.km1818.com/10/c-list-14751.html"
# ,"http://search.km1818.com/10/c-list-14766.html"
# ,"http://search.km1818.com/10/c-list-14767.html"
# ,"http://search.km1818.com/10/c-list-14768.html"
# ,"http://search.km1818.com/10/c-list-14769.html"
# ,"http://search.km1818.com/10/c-list-14771.html"
# ,"http://search.km1818.com/10/c-list-14772.html"
# ,"http://search.km1818.com/10/c-list-14773.html"
# ,"http://search.km1818.com/10/c-list-14774.html"
# ,"http://search.km1818.com/10/c-list-14775.html"
# ,"http://search.km1818.com/10/c-list-14747.html"
# ,"http://search.km1818.com/10/c-list-14748.html"
# ,"http://search.km1818.com/10/c-list-14752.html"
# ,"http://search.km1818.com/10/c-list-14746.html"
# ,"http://search.km1818.com/10/c-list-8150.html"
# ,"http://search.km1818.com/10/c-list-8155.html"
# ,"http://search.km1818.com/10/c-list-8158.html"
# ,"http://search.km1818.com/10/c-list-8162.html"
# ,"http://search.km1818.com/10/c-list-8163.html"
# ,"http://search.km1818.com/10/c-list-8151.html"
# ,"http://search.km1818.com/10/c-list-8153.html"
# ,"http://search.km1818.com/10/c-list-8156.html"
# ,"http://search.km1818.com/10/c-list-8160.html"
# ,"http://search.km1818.com/10/c-list-8161.html"
# ,"http://search.km1818.com/10/c-list-8152.html"
# ,"http://search.km1818.com/10/c-list-8154.html"
# ,"http://search.km1818.com/10/c-list-8157.html"
# ,"http://search.km1818.com/10/c-list-8159.html"
# ,"http://search.km1818.com/10/c-list-14780.html"
# ,"http://search.km1818.com/10/c-list-14781.html"
# ,"http://search.km1818.com/10/c-list-14783.html"
# ,"http://search.km1818.com/10/c-list-14779.html"
# ,"http://search.km1818.com/10/c-list-14782.html"
# ,"http://search.km1818.com/10/c-list-14784.html"
# ,"http://search.km1818.com/10/c-list-14785.html"
# ,"http://search.km1818.com/10/c-list-8184.html"
# ,"http://search.km1818.com/10/c-list-14787.html"
# ,"http://search.km1818.com/10/c-list-14788.html"
# ,"http://search.km1818.com/10/c-list-8182.html"
# ,"http://search.km1818.com/10/c-list-14792.html"
# ,"http://search.km1818.com/10/c-list-14790.html"
# ,"http://search.km1818.com/10/c-list-14789.html"
# ,"http://search.km1818.com/10/c-list-14786.html"
# ,"http://search.km1818.com/10/c-list-14759.html"
# ,"http://search.km1818.com/10/c-list-14757.html"
# ,"http://search.km1818.com/10/c-list-14756.html"
# ,"http://search.km1818.com/10/c-list-14758.html"
# ,"http://search.km1818.com/10/c-list-14760.html"
# ,"http://search.km1818.com/10/c-list-14754.html"
# ,"http://search.km1818.com/10/c-list-14755.html"
# ,"http://search.km1818.com/10/c-list-14793.html"
# ,"http://search.km1818.com/10/c-list-8170.html"
# ,"http://search.km1818.com/10/c-list-14795.html"
# ,"http://search.km1818.com/10/c-list-14796.html"
# ,"http://search.km1818.com/10/c-list-8165.html"
# ,"http://search.km1818.com/10/c-list-8167.html"
# ,"http://search.km1818.com/10/c-list-8169.html"
# ,"http://search.km1818.com/10/c-list-8166.html"
# ,"http://search.km1818.com/10/c-list-8172.html"
# ,"http://search.km1818.com/10/c-list-14794.html"
# ,"http://search.km1818.com/10/c-list-14797.html"
# ,"http://search.km1818.com/10/c-list-8168.html"
# ,"http://search.km1818.com/10/c-list-8171.html"
# ,"http://search.km1818.com/10/c-list-9002.html"
# ,"http://search.km1818.com/10/c-list-8193.html"
# ,"http://search.km1818.com/10/c-list-8192.html"
# ,"http://search.km1818.com/10/c-list-8562.html"
# ,"http://search.km1818.com/10/c-list-14761.html"
# ,"http://search.km1818.com/10/c-list-14762.html"
# ,"http://search.km1818.com/10/c-list-14764.html"]
    three_url_list=[]
    base_url = "http://search.km1818.com/"
    start_urls = [base_url]
    def parse(self, response):
        # 提取所有二级url
        print("parse in*****************************")
        two_list = response.xpath("//div[@class='box-lis-item']/dl/dd/em/a/@href").extract()
        # 一级标题先提取出来

        for two_url in two_list:
            print("parse out*****************************")
            yield scrapy.Request(two_url, callback=self.parse_two)

    def parse_two(self, response):
        print("parse_two in*****************************")
        # # 二级页面的内容
        # node_list = response.xpath("//div[@class='m-prosales-cont']/ul")
        # 一级标题
        one_title = response.xpath("/html/body/div[3]/h1/a/text()").extract_first()
        two = response.xpath("/html/body/div[3]/span[1]/a[1]/text()").extract_first()
        two_path = response.xpath("/html/body/div[3]/span[1]/a[1]/@href").extract_first()
        if two_path is not str:
            two_path = str(two_path)
        two_url = self.base_url+"10/"+two_path
        three = response.xpath("/html/body/div[3]/span[2]/a[1]/text()").extract_first()
        # 三级url列表
        three_list = response.xpath("//div[@class='m-prosales-cont']/ul/li/div[2]/a/@href").extract()
        for three_url in three_list:
            print("parse_two out*****************************")
            yield scrapy.Request(three_url, callback=self.parse_three, meta={"two":two,"two_url":two_url,"three":three,"three_url":three_url,"one_title":one_title})
        # # 遍历２级页面，提取字段内容
        # for node in node_list:
        #     item = KmmallItem()
        #     item['one'] = response.xpath("/html/body/div[3]/h1/a/text()").extract_first()
        #     item['two'] = response.xpath("/html/body/div[3]/span[1]/a/text()").extract_first()
        #     item['two_url'] = self.base_url+response.xpath("/html/body/div[3]/span[1]/a/@href").extract_first()
        #     item['three'] = response.xpath("/html/body/div[3]/span[2]/a/text()").extract_first()
        #     item['three_url'] = self.base_url+response.xpath("/html/body/div[3]/span[2]/a/@href").extract_first()
        #     li_list = node.xpath('./li')
        #     for li in li_list:
        #         item['title'] = li.xpath('./div/a/@title').extract_first()
        #         item['goods_url'] = li.xpath('./div[1]/a/@href').extract_first()
        #         item['price'] = li.xpath('./div[3]/strong/text()').extract_first()
        #         # item['head'] = li.xpath("normalize-space(//div[@class='m-prosales-cont']/ul[1]/li[1]/div[2]/a/text())").extract_first()
        #         item['head'] = li.xpath("./div[2]/a/text()").extract_first()

    def parse_three(self, response):
        print("parse_three in*****************************")
        item = KmmallItem()
        node=response.xpath("//div[@class='product-intro']")
        item['one']=response.meta['one_title']
        item['two'] = response.meta['two']
        item['two_url'] = response.meta['two_url']
        item['three'] = response.meta['three']
        item['three_url'] = response.meta['three_url']
        item['title'] = node.xpath("./div[2]/div[1]/h1/text()").extract_first()
        item['title_two'] = response.xpath("/html/body/div[6]/div[1]/div[2]/div[1]/h1/span/text()").extract_first()
        item['goods_url'] = response.meta['three_url']
        item['price'] = node.xpath("./div[2]/div[2]/div[1]/ul[1]/li[3]//label/text()").extract_first()
        item['market_price'] = node.xpath("./div[2]/div[2]/div[1]/ul[1]/li[4]//del/text()").extract_first()
        item['spec'] = node.xpath("./div[2]/div[2]/div[1]/ul[1]/li[7]/dd/a/text()").extract_first()
        item['count_comment'] = node.xpath("./div[2]/div[2]/div[1]/ul[1]/li[5]//label/text()").extract_first()
        item['goods_name'] = response.xpath("//ul[@class='detail-list']/li[1]/text()").extract_first()
        item['goods_no'] = response.xpath("//ul[@class='detail-list']/li[2]/text()").extract_first()
        item['goods_pz'] = response.xpath("//ul[@class='detail-list']/li[3]/text()").extract_first()
        item['goods_logo'] = response.xpath("//ul[@class='detail-list']/li[4]/text()").extract_first()
        item['goods_spec'] = response.xpath("//ul[@class='detail-list']/li[5]/text()").extract_first()
        item['goods_jx'] = response.xpath("//ul[@class='detail-list']/li[6]/text()").extract_first()
        item['goods_cj'] = response.xpath("//ul[@class='detail-list']/li[7]/text()").extract_first()
        print("parse_three out*****************************")
        yield item








